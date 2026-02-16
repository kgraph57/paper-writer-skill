#!/usr/bin/env bash
# compile-manuscript.sh - Compiles markdown manuscript sections into a single document.
#
# Usage: ./compile-manuscript.sh /path/to/project-dir [output-format]
# Formats: md (default), docx, pdf, latex
#
# Reads sections in order: Title, Abstract, Keywords, Introduction, Methods,
# Results, Discussion, Conclusion, References, Appendices
# Strips TODO/NOTE/FIXME comments, adds page breaks, generates line-numbered version.

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"
VERSION="1.0.0"

SECTION_ORDER=(
    "Title Page:title"
    "Abstract:abstract"
    "Keywords:keywords"
    "Introduction:introduction"
    "Methods:methods"
    "Results:results"
    "Discussion:discussion"
    "Conclusion:conclusion"
    "Acknowledgments:acknowledgments"
    "Declarations:declarations"
    "References:references"
    "Appendices:appendix"
    "Supplementary:supplementary"
    "Tables:tables"
    "Figures:figures"
    "Figure Legends:figure-legends"
)

usage() {
    echo "${SCRIPT_NAME} v${VERSION} - Compile manuscript sections"
    echo ""
    echo "USAGE: ${SCRIPT_NAME} <project-dir> [output-format]"
    echo ""
    echo "  project-dir     Directory containing section .md files"
    echo "  output-format   md (default), docx, pdf, latex"
    echo ""
    echo "EXAMPLES:"
    echo "  ${SCRIPT_NAME} ./my-paper"
    echo "  ${SCRIPT_NAME} ./my-paper docx"
    echo "  ${SCRIPT_NAME} ./my-paper pdf"
    echo ""
    echo "SECTIONS (in order):"
    for section in "${SECTION_ORDER[@]}"; do
        IFS=':' read -r name pattern <<< "${section}"
        printf "  %-20s (%s.md)\n" "${name}" "${pattern}"
    done
    echo ""
    echo "NOTES:"
    echo "  - TODO/NOTE/FIXME lines and HTML comments are stripped"
    echo "  - pandoc required for docx/pdf/latex; LaTeX required for pdf"
}

log_info() { echo "[INFO] $*"; }
log_warn() { echo "[WARN] $*" >&2; }
log_error() { echo "[ERROR] $*" >&2; }

check_pandoc() {
    if ! command -v pandoc &>/dev/null; then
        log_error "pandoc not installed. Required for ${1} output."
        log_error "Install: brew install pandoc (macOS) or apt install pandoc (Linux)"
        return 1
    fi
}

check_latex() {
    if ! command -v pdflatex &>/dev/null && ! command -v xelatex &>/dev/null; then
        log_error "LaTeX not found. Required for PDF output."
        return 1
    fi
}

find_section_file() {
    local project_dir="$1" pattern="$2"
    if [[ -f "${project_dir}/${pattern}.md" ]]; then
        echo "${project_dir}/${pattern}.md"
        return 0
    fi
    local globs=("${project_dir}/${pattern}"*.md "${project_dir}"/[0-9]*"_${pattern}"*.md "${project_dir}"/[0-9]*"-${pattern}"*.md)
    for g in "${globs[@]}"; do
        if [[ -f "$g" ]]; then
            echo "$g"
            return 0
        fi
    done
    return 1
}

strip_internal_notes() {
    local f="$1"
    perl -0777 -pe 's/<!--.*?-->//gs' "$f" | \
        grep -vE '^\s*(TODO|FIXME|HACK|XXX|NOTE|INTERNAL):' 2>/dev/null | \
        cat -s
}

main() {
    if [[ $# -lt 1 ]] || [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
        usage; exit 0
    fi

    local project_dir="$1"
    local output_format="${2:-md}"

    if [[ ! -d "${project_dir}" ]]; then
        log_error "Directory not found: ${project_dir}"; exit 1
    fi

    project_dir="$(cd "${project_dir}" && pwd)"
    local project_name; project_name="$(basename "${project_dir}")"
    local ts; ts="$(date +%Y%m%d_%H%M%S)"
    local outbase="${project_dir}/compiled/${project_name}_manuscript_${ts}"
    local out_md="${outbase}.md"
    local out_numbered="${outbase}_numbered.md"

    mkdir -p "${project_dir}/compiled"
    log_info "Compiling from: ${project_dir}"
    log_info "Format: ${output_format}"

    local tmp; tmp=$(mktemp)
    trap "rm -f '${tmp}'" EXIT

    local found=0
    local missing=()

    for entry in "${SECTION_ORDER[@]}"; do
        IFS=':' read -r sec_name sec_pat <<< "${entry}"
        local sec_file
        if sec_file=$(find_section_file "${project_dir}" "${sec_pat}"); then
            log_info "Found: ${sec_name} -> $(basename "${sec_file}")"
            if [[ ${found} -gt 0 ]]; then
                printf '\n\n---\n\n\\newpage\n\n' >> "${tmp}"
            fi
            strip_internal_notes "${sec_file}" >> "${tmp}"
            ((found++))
        else
            missing+=("${sec_name}")
        fi
    done

    echo ""
    log_info "=== Compilation Summary ==="
    log_info "Sections included: ${found}"
    if [[ ${#missing[@]} -gt 0 ]]; then
        log_warn "Sections not found (skipped):"
        for m in "${missing[@]}"; do log_warn "  - ${m}"; done
    fi
    if [[ ${found} -eq 0 ]]; then
        log_error "No sections found."; exit 1
    fi

    cp "${tmp}" "${out_md}"
    log_info "Written: ${out_md}"

    nl -ba -w4 -s'  ' "${tmp}" > "${out_numbered}"
    log_info "Written (numbered): ${out_numbered}"

    case "${output_format}" in
        md) log_info "Markdown output complete." ;;
        docx)
            if check_pandoc "docx"; then
                local out_docx="${outbase}.docx"
                if [[ -f "${project_dir}/reference.docx" ]]; then
                    pandoc "${out_md}" -f markdown -t docx --toc \
                        --reference-doc="${project_dir}/reference.docx" -o "${out_docx}"
                else
                    pandoc "${out_md}" -f markdown -t docx --toc -o "${out_docx}"
                fi
                log_info "Written: ${out_docx}"
            fi ;;
        pdf)
            if check_pandoc "pdf" && check_latex; then
                local out_pdf="${outbase}.pdf"
                local engine="xelatex"
                command -v xelatex &>/dev/null || engine="pdflatex"
                pandoc "${out_md}" -f markdown --pdf-engine="${engine}" --toc \
                    -V geometry:margin=1in -V fontsize=12pt -V linestretch=2 \
                    -o "${out_pdf}"
                log_info "Written: ${out_pdf}"
            fi ;;
        latex|tex)
            if check_pandoc "LaTeX"; then
                local out_tex="${outbase}.tex"
                pandoc "${out_md}" -f markdown -t latex --standalone --toc \
                    -V geometry:margin=1in -V fontsize=12pt -V linestretch=2 \
                    -o "${out_tex}"
                log_info "Written: ${out_tex}"
            fi ;;
        *) log_error "Unknown format: ${output_format}. Use: md, docx, pdf, latex"; exit 1 ;;
    esac

    local wc_w; wc_w=$(wc -w < "${tmp}" | tr -d ' ')
    local wc_c; wc_c=$(wc -c < "${tmp}" | tr -d ' ')
    echo ""
    log_info "=== Manuscript Statistics ==="
    log_info "Word count:      ${wc_w}"
    log_info "Character count: ${wc_c}"
    log_info "Sections:        ${found}"
    log_info "Compilation complete."
}

main "$@"
