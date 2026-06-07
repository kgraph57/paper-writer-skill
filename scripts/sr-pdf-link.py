#!/usr/bin/env python3
"""
SR PDF Linker — links full-text PDFs to screening records and renames them.

For full-text screening you need each PDF tied to its bibliographic record.
Filenames from publishers are useless ("nihms-1234.pdf", "1-s2.0-....pdf").
This script reads the DOI out of each PDF, joins it to the records CSV by DOI,
and (optionally) renames matched PDFs to a canonical, sortable name. It NEVER
deletes or overwrites originals — renames are copies into a `renamed/` subfolder.

It also reports the two gaps that feed the PRISMA diagram:
  - include-records with NO matching PDF  → "reports not retrieved"
  - PDFs that match NO record             → check manually (wrong file? not searched?)

Usage:
    python sr-pdf-link.py --pdfs full-texts/ --records 02_title_abstract_screen.csv
    python sr-pdf-link.py --pdfs full-texts/ --records 02_title_abstract_screen.csv \
        --include-only --rename

DOI extraction is robust (DOIs are unique + machine-readable); title guessing
from PDFs is not, so this script joins on DOI only. Records without a DOI must
be linked manually.
"""

import argparse
import csv
import os
import re
import shutil
import sys

csv.field_size_limit(10_000_000)

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\])}]+", re.IGNORECASE)


def norm_doi(doi):
    if not doi:
        return ""
    d = doi.strip().lower().rstrip(".,;)")
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:\s*", "", d)
    return d


def extract_text_first_pages(path, pages=2):
    """Try pypdf, then pdfplumber. Return concatenated text of first N pages."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        txt = []
        for p in reader.pages[:pages]:
            txt.append(p.extract_text() or "")
        if any(t.strip() for t in txt):
            return "\n".join(txt)
    except Exception:
        pass
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            return "\n".join((pg.extract_text() or "")
                             for pg in pdf.pages[:pages])
    except Exception as e:
        print(f"  ! Could not read {os.path.basename(path)}: {e}", file=sys.stderr)
        return ""


def doi_from_pdf(path):
    text = extract_text_first_pages(path)
    m = DOI_RE.search(text or "")
    return norm_doi(m.group(0)) if m else ""


def first_author_surname(authors):
    if not authors:
        return "NA"
    first = re.split(r"[;]", authors)[0].strip()
    if "," in first:
        surname = first.split(",")[0]
    else:
        parts = first.split()
        surname = parts[0] if parts else "NA"
    surname = re.sub(r"[^A-Za-z]", "", surname)
    return surname or "NA"


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", (s or "")).strip("-")


def main():
    ap = argparse.ArgumentParser(description="Link full-text PDFs to records by DOI")
    ap.add_argument("--pdfs", required=True, help="Folder of PDFs")
    ap.add_argument("--records", required=True, help="Records CSV (01 or 02 stage)")
    ap.add_argument("--include-only", action="store_true",
                    help="Only expect PDFs for records with consensus_decision=include")
    ap.add_argument("--rename", action="store_true",
                    help="Copy matched PDFs to <pdfs>/renamed/ with canonical names")
    ap.add_argument("--output", help="Link map CSV (default: <pdfs>/pdf-link-map.csv)")
    args = ap.parse_args()

    if not os.path.isdir(args.pdfs):
        sys.exit(f"PDF folder not found: {args.pdfs}")
    if not os.path.isfile(args.records):
        sys.exit(f"Records CSV not found: {args.records}")

    with open(args.records, newline="", encoding="utf-8-sig", errors="replace") as f:
        records = list(csv.DictReader(f))

    def is_target(r):
        if r.get("dup_of"):
            return False
        if args.include_only:
            return (r.get("consensus_decision") or "").strip().lower().startswith("inc")
        return True

    targets = [r for r in records if is_target(r)]
    by_doi = {norm_doi(r.get("doi")): r for r in targets if norm_doi(r.get("doi"))}

    pdfs = [os.path.join(args.pdfs, n) for n in sorted(os.listdir(args.pdfs))
            if n.lower().endswith(".pdf") and os.path.isfile(os.path.join(args.pdfs, n))]

    rename_dir = os.path.join(args.pdfs, "renamed")
    if args.rename:
        os.makedirs(rename_dir, exist_ok=True)

    link_rows = []
    matched_record_ids = set()
    unmatched_pdfs = []

    for path in pdfs:
        base = os.path.basename(path)
        doi = doi_from_pdf(path)
        rec = by_doi.get(doi) if doi else None
        if rec:
            rid = rec.get("record_id", "")
            matched_record_ids.add(rid)
            new_name = ""
            if args.rename:
                tag = rec.get("pmid") or slug(doi) or rid
                new_name = f"{first_author_surname(rec.get('authors'))}_{rec.get('year','')}_{tag}.pdf"
                shutil.copy2(path, os.path.join(rename_dir, new_name))
            link_rows.append({"record_id": rid, "doi": doi, "title": rec.get("title", ""),
                              "pdf_file": base, "renamed_to": new_name, "status": "matched"})
            print(f"  matched  {base}  ->  {rid}" +
                  (f"  ({new_name})" if new_name else ""))
        else:
            unmatched_pdfs.append(base)
            link_rows.append({"record_id": "", "doi": doi, "title": "",
                              "pdf_file": base, "renamed_to": "",
                              "status": "no_doi" if not doi else "doi_not_in_records"})
            print(f"  UNMATCHED {base}  (doi={doi or 'none found'})")

    not_retrieved = [r for r in targets if r.get("record_id") not in matched_record_ids]

    out = args.output or os.path.join(args.pdfs, "pdf-link-map.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["record_id", "doi", "title",
                                          "pdf_file", "renamed_to", "status"])
        w.writeheader()
        w.writerows(link_rows)
        for r in not_retrieved:
            w.writerow({"record_id": r.get("record_id", ""),
                        "doi": norm_doi(r.get("doi")), "title": r.get("title", ""),
                        "pdf_file": "", "renamed_to": "", "status": "not_retrieved"})

    print("\n=== PDF link summary ===")
    print(f"  PDFs in folder:            {len(pdfs)}")
    print(f"  Matched to records:        {len(matched_record_ids)}")
    print(f"  PDFs matching no record:   {len(unmatched_pdfs)}")
    print(f"  Records with no PDF:       {len(not_retrieved)}  "
          f"(\"reports not retrieved\" = {len(not_retrieved)})")
    print(f"\nWrote link map: {out}")
    if args.rename:
        print(f"Renamed copies in: {rename_dir}")
    if unmatched_pdfs:
        print("\nUnmatched PDFs need a manual DOI check:")
        for n in unmatched_pdfs:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
