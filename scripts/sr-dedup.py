#!/usr/bin/env python3
"""
SR De-duplicator — Stage 1 of the screening pipeline.

Parses raw database exports (RIS, NBIB/MEDLINE, BibTeX, CSV), normalizes
DOI/title, removes duplicates, and writes an auditable deduplicated CSV plus
PRISMA identification counts.

Usage:
    python sr-dedup.py --input 00_imported/ --output 01_deduplicated.csv \
        --counts counts/identification.json
    python sr-dedup.py --input 00_imported/ --output 01_deduplicated.csv --fuzzy 0.95

De-duplication logic (deterministic, no LLM):
    1. Exact match on normalized DOI
    2. Exact match on normalized title
    3. Fuzzy title match (difflib ratio >= --fuzzy, default 0.92) within same year

Output CSV keeps EVERY record (auditable). Kept records have an empty `dup_of`;
removed records carry the `record_id` of the canonical record they merged into.

Input formats (by extension):
    .nbib / .txt (MEDLINE)  — PubMed export
    .ris                    — Scopus, EMBASE, CINAHL, Cochrane, etc.
    .bib                    — BibTeX
    .csv                    — generic (header names auto-mapped)
"""

import argparse
import csv
import json
import os
import re
import sys
from difflib import SequenceMatcher

csv.field_size_limit(10_000_000)

FIELDS = ["record_id", "doi", "pmid", "title", "authors", "year",
          "journal", "abstract", "source_db", "dup_of"]


# ----------------------------- normalization ------------------------------ #

def norm_doi(doi):
    if not doi:
        return ""
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d.strip()


def norm_title(title):
    if not title:
        return ""
    t = title.lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def year_of(raw):
    if not raw:
        return ""
    m = re.search(r"(19|20)\d{2}", str(raw))
    return m.group(0) if m else ""


def first_doi_in(text):
    m = re.search(r"10\.\d{4,9}/[^\s\"'<>\])]+", text or "")
    return norm_doi(m.group(0)) if m else ""


# ------------------------------- parsers ---------------------------------- #

def parse_medline(text, source):
    """PubMed MEDLINE / .nbib format (TAG- value, 6-space continuation)."""
    records, cur, last_tag = [], {}, None
    for line in text.splitlines():
        if not line.strip():
            if cur:
                records.append(_finish_medline(cur, source))
                cur, last_tag = {}, None
            continue
        m = re.match(r"^([A-Z][A-Z0-9 ]{1,4})- (.*)$", line)
        if m:
            tag = m.group(1).strip()
            cur.setdefault(tag, []).append(m.group(2).strip())
            last_tag = tag
        elif line.startswith("      ") and last_tag:
            cur[last_tag][-1] += " " + line.strip()
    if cur:
        records.append(_finish_medline(cur, source))
    return records


def _finish_medline(cur, source):
    doi = ""
    for tag in ("LID", "AID"):
        for v in cur.get(tag, []):
            if "[doi]" in v.lower():
                doi = first_doi_in(v)
                break
        if doi:
            break
    return {
        "doi": doi,
        "pmid": (cur.get("PMID", [""])[0]).strip(),
        "title": " ".join(cur.get("TI", [])).strip(),
        "authors": "; ".join(cur.get("FAU", cur.get("AU", []))),
        "year": year_of(cur.get("DP", [""])[0]),
        "journal": (cur.get("JT", cur.get("TA", [""]))[0]).strip(),
        "abstract": " ".join(cur.get("AB", [])).strip(),
        "source_db": source,
    }


def parse_ris(text, source):
    """RIS format (TY  - JOUR ... ER  -)."""
    records, cur, last_tag = [], {}, None
    for line in text.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9]) {2}- ?(.*)$", line)
        if m:
            tag, val = m.group(1), m.group(2).strip()
            if tag == "TY":
                cur, last_tag = {}, None
                cur["TY"] = [val]
            elif tag == "ER":
                if cur:
                    records.append(_finish_ris(cur, source))
                cur, last_tag = {}, None
            else:
                cur.setdefault(tag, []).append(val)
                last_tag = tag
        elif line.strip() and last_tag:
            cur[last_tag][-1] += " " + line.strip()
    if cur.get("TY"):
        records.append(_finish_ris(cur, source))
    return records


def _finish_ris(cur, source):
    doi = norm_doi((cur.get("DO", cur.get("DI", [""]))[0]))
    if not doi:
        doi = first_doi_in(" ".join(cur.get("UR", []) + cur.get("L3", [])))
    pmid = ""
    for tag in ("AN", "ID", "C7"):
        for v in cur.get(tag, []):
            if v.isdigit() and 6 <= len(v) <= 9:
                pmid = v
                break
        if pmid:
            break
    journal = (cur.get("JO", cur.get("JF", cur.get("T2", cur.get("JA", [""]))))[0]).strip()
    return {
        "doi": doi,
        "pmid": pmid,
        "title": " ".join(cur.get("TI", cur.get("T1", []))).strip(),
        "authors": "; ".join(cur.get("AU", cur.get("A1", []))),
        "year": year_of((cur.get("PY", cur.get("Y1", cur.get("DA", [""]))))[0]),
        "journal": journal,
        "abstract": " ".join(cur.get("AB", cur.get("N2", []))).strip(),
        "source_db": source,
    }


def parse_bibtex(text, source):
    records = []
    for entry in re.split(r"@\w+\s*\{", text)[1:]:
        def field(name):
            m = re.search(name + r"\s*=\s*[{\"](.+?)[}\"]\s*,?\s*\n",
                          entry, re.IGNORECASE | re.DOTALL)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
        records.append({
            "doi": norm_doi(field("doi")),
            "pmid": field("pmid"),
            "title": field("title").strip("{} "),
            "authors": field("author"),
            "year": year_of(field("year")),
            "journal": field("journal") or field("journaltitle"),
            "abstract": field("abstract"),
            "source_db": source,
        })
    return records


CSV_MAP = {
    "doi": ["doi", "do", "di"],
    "pmid": ["pmid", "pubmed id", "pubmed_id", "an"],
    "title": ["title", "ti", "article title", "primary title"],
    "authors": ["authors", "author", "au", "creator"],
    "year": ["year", "py", "dp", "publication year", "date"],
    "journal": ["journal", "source title", "source", "jo", "jf",
                "journal title", "publication title"],
    "abstract": ["abstract", "ab", "n2"],
}


def parse_csv(path, source):
    records = []
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        lower = {(h or "").strip().lower(): h for h in (reader.fieldnames or [])}

        def pick(keys):
            for k in keys:
                if k in lower:
                    return lower[k]
            return None
        cols = {field: pick(keys) for field, keys in CSV_MAP.items()}
        for row in reader:
            rec = {f: (row.get(cols[f], "") or "").strip() if cols[f] else ""
                   for f in CSV_MAP}
            rec["doi"] = norm_doi(rec["doi"])
            rec["year"] = year_of(rec["year"])
            rec["source_db"] = source
            records.append(rec)
    return records


def parse_file(path):
    source = os.path.splitext(os.path.basename(path))[0]
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return parse_csv(path, source)
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        text = f.read()
    if ext in (".nbib",) or (ext == ".txt" and re.search(r"^PMID- ", text, re.M)):
        return parse_medline(text, source)
    if ext == ".ris" or re.search(r"^TY {2}- ", text, re.M):
        return parse_ris(text, source)
    if ext == ".bib" or text.lstrip().startswith("@"):
        return parse_bibtex(text, source)
    if re.search(r"^PMID- ", text, re.M):
        return parse_medline(text, source)
    print(f"  ! Unrecognized format, skipped: {path}", file=sys.stderr)
    return []


# ------------------------------ union-find -------------------------------- #

class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def completeness(rec):
    return sum(1 for k in ("doi", "pmid", "abstract", "journal", "year")
               if rec.get(k))


# --------------------------------- main ----------------------------------- #

def main():
    ap = argparse.ArgumentParser(description="SR de-duplicator (Stage 1)")
    ap.add_argument("--input", required=True, help="Folder of raw DB exports")
    ap.add_argument("--output", required=True, help="01_deduplicated.csv path")
    ap.add_argument("--counts", help="identification.json path")
    ap.add_argument("--fuzzy", type=float, default=0.92,
                    help="Fuzzy title match threshold (default 0.92)")
    args = ap.parse_args()

    if not os.path.isdir(args.input):
        sys.exit(f"Input folder not found: {args.input}")

    records, db_counts = [], {}
    for name in sorted(os.listdir(args.input)):
        path = os.path.join(args.input, name)
        if not os.path.isfile(path) or name.startswith("."):
            continue
        if os.path.splitext(name)[1].lower() not in (".ris", ".nbib", ".bib",
                                                     ".csv", ".txt"):
            continue
        recs = parse_file(path)
        if recs:
            db_counts[recs[0]["source_db"]] = len(recs)
            records.extend(recs)
            print(f"  parsed {len(recs):>5} from {name}")

    n = len(records)
    if n == 0:
        sys.exit("No records parsed. Check input formats.")
    for i, r in enumerate(records):
        r["record_id"] = f"R{i + 1:04d}"
        r["norm_doi"] = norm_doi(r.get("doi"))
        r["norm_title"] = norm_title(r.get("title"))

    uf = UF(n)
    by_doi, by_title = {}, {}
    for i, r in enumerate(records):
        if r["norm_doi"]:
            if r["norm_doi"] in by_doi:
                uf.union(i, by_doi[r["norm_doi"]])
            else:
                by_doi[r["norm_doi"]] = i
        if r["norm_title"]:
            if r["norm_title"] in by_title:
                uf.union(i, by_title[r["norm_title"]])
            else:
                by_title[r["norm_title"]] = i

    # Fuzzy title match within year buckets (only records not already DOI-linked)
    buckets = {}
    for i, r in enumerate(records):
        if r["norm_title"]:
            buckets.setdefault(r["year"], []).append(i)
    for idxs in buckets.values():
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                i, j = idxs[a], idxs[b]
                if uf.find(i) == uf.find(j):
                    continue
                ti, tj = records[i]["norm_title"], records[j]["norm_title"]
                if abs(len(ti) - len(tj)) > max(len(ti), len(tj)) * 0.3:
                    continue
                if SequenceMatcher(None, ti, tj).ratio() >= args.fuzzy:
                    uf.union(i, j)

    clusters = {}
    for i in range(n):
        clusters.setdefault(uf.find(i), []).append(i)

    for members in clusters.values():
        canon = max(members, key=lambda i: (completeness(records[i]), -i))
        canon_id = records[canon]["record_id"]
        for i in members:
            records[i]["dup_of"] = "" if i == canon else canon_id

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in records:
            w.writerow(r)

    kept = sum(1 for r in records if not r["dup_of"])
    removed = n - kept
    counts = {
        "db_counts": db_counts,
        "total_identified": n,
        "duplicates_removed": removed,
        "records_after_dedup": kept,
        "fuzzy_threshold": args.fuzzy,
    }
    if args.counts:
        os.makedirs(os.path.dirname(os.path.abspath(args.counts)), exist_ok=True)
        with open(args.counts, "w", encoding="utf-8") as f:
            json.dump(counts, f, indent=2, ensure_ascii=False)

    print("\n=== De-duplication summary ===")
    for db, c in db_counts.items():
        print(f"  {db:<20} {c:>6}")
    print(f"  {'TOTAL identified':<20} {n:>6}")
    print(f"  {'Duplicates removed':<20} {removed:>6}")
    print(f"  {'Records after dedup':<20} {kept:>6}")
    print(f"\nWrote {args.output}" + (f" and {args.counts}" if args.counts else ""))


if __name__ == "__main__":
    main()
