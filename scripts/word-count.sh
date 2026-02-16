#!/usr/bin/env bash
#
# word-count.sh - Track word counts per section for academic papers
#
# Counts words in each section file (02-08 .md files), strips markdown
# formatting before counting, compares against configurable journal limits,
# and outputs a formatted summary table.
#
# Usage:
#   ./word-count.sh /path/to/project-dir [journal-preset]
#
# Arguments:
#   project-dir     Path to the paper project directory containing .md files
#   journal-preset  Optional journal name for word limits (default: custom)
#
# Available journal presets:
#   jmir         - JMIR (Journal of Medical Internet Research): 3500 words
#   bmj-open     - BMJ Open: 4000 words
#   lancet       - The Lancet: 3000 words
#   nejm         - New England Journal of Medicine: 2500 words
#   jama         - JAMA: 3000 words
#   plos-one     - PLOS ONE: no limit (reports only)
#   nature       - Nature: 3000 words (Article)
#   bmj          - BMJ: 4000 words
#   annals       - Annals of Internal Medicine: 3000 words
#   cochrane     - Cochrane Systematic Reviews: no strict limit
#   custom       - Use default generous limits per section
#
# Examples:
#   ./word-count.sh ~/papers/my-systematic-review
#   ./word-count.sh ~/papers/my-systematic-review jmir
#   ./word-count.sh ~/papers/my-systematic-review bmj-open
#   ./word-count.sh . custom
#
# Section files expected (standard paper-writer project structure):
#   02-introduction.md
#   03-methods.md
#   04-results.md
#   05-discussion.md
#   06-conclusion.md
#   07-references.md  (excluded from word count)
#   08-appendix.md    (excluded from word count, or counted separately)
#   01-abstract.md    (counted separately, not toward body total)
#
# The script strips the following markdown elements before counting:
#   - YAML front matter (--- blocks)
#   - Markdown headers (# ## ### etc.)
#   - Bold/italic markers (** * __ _)
#   - Links [text](url) -> counts only "text"
#   - Images ![alt](url) -> excluded
#   - HTML tags
#   - Code blocks (``` ... ```)
#   - Inline code (`code`)
#   - Block quotes (> )
#   - List markers (- * 1.)
#   - Horizontal rules (--- ***)
#   - Empty lines
#   - Comment lines (<!-- -->)

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

PROJECT_DIR="${1:-.}"
JOURNAL_PRESET="${2:-custom}"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# ============================================================================
# Journal Presets (total body word limits and per-section guidance)
# Format: TOTAL ABSTRACT INTRO METHODS RESULTS DISCUSSION CONCLUSION
# ============================================================================

get_journal_limits() {
    local journal="$1"
    case "$journal" in
        jmir)
            echo "3500 300 500 1000 1000 800 200"
            ;;
        bmj-open)
            echo "4000 300 600 1200 1200 800 200"
            ;;
        lancet)
            echo "3000 300 400 800 900 700 200"
            ;;
        nejm)
            echo "2500 250 400 700 700 500 200"
            ;;
        jama)
            echo "3000 350 400 900 900 600 200"
            ;;
        plos-one)
            echo "0 300 0 0 0 0 0"
            ;;
        nature)
            echo "3000 150 400 800 900 700 200"
            ;;
        bmj)
            echo "4000 300 600 1200 1200 800 200"
            ;;
        annals)
            echo "3000 300 400 800 900 700 200"
            ;;
        cochrane)
            echo "0 400 0 0 0 0 0"
            ;;
        custom|*)
            echo "5000 350 800 1500 1500 1000 300"
            ;;
    esac
}

# ============================================================================
# Word counting function (strips markdown formatting)
# ============================================================================

count_words_in_file() {
    local file="$1"

    if [ ! -f "$file" ]; then
        echo "0"
        return
    fi

    # Strip markdown formatting and count words
    sed \
        -e '/^---$/,/^---$/d' \
        -e '/^```/,/^```/d' \
        -e '/^<!--/,/-->$/d' \
        -e 's/^#\+ //' \
        -e 's/!\[[^]]*\]([^)]*)//g' \
        -e 's/\[[^]]*\]([^)]*)//g' \
        -e 's/\[([^]]*)\]/\1/g' \
        -e 's/<[^>]*>//g' \
        -e 's/\*\*//g' \
        -e 's/\*//g' \
        -e 's/__//g' \
        -e 's/_//g' \
        -e 's/`[^`]*`//g' \
        -e 's/^> //' \
        -e 's/^[[:space:]]*[-*+] //' \
        -e 's/^[[:space:]]*[0-9]\+\. //' \
        -e '/^[[:space:]]*$/d' \
        -e '/^---$/d' \
        -e '/^\*\*\*$/d' \
        "$file" | wc -w | tr -d '[:space:]'
}

# ============================================================================
# Main
# ============================================================================

# Validate project directory
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}Error: Directory not found: $PROJECT_DIR${NC}" >&2
    exit 1
fi

# Get journal limits
LIMITS=$(get_journal_limits "$JOURNAL_PRESET")
read -r LIMIT_TOTAL LIMIT_ABSTRACT LIMIT_INTRO LIMIT_METHODS LIMIT_RESULTS LIMIT_DISCUSSION LIMIT_CONCLUSION <<< "$LIMITS"

# Define section files and their names
declare -a SECTION_FILES
declare -a SECTION_NAMES
declare -a SECTION_LIMITS

# Look for section files in standard naming patterns
find_section_file() {
    local pattern="$1"
    local dir="$PROJECT_DIR"
    # Try common patterns
    for f in "$dir"/$pattern; do
        if [ -f "$f" ]; then
            echo "$f"
            return
        fi
    done
    echo ""
}

# Map section files
ABSTRACT_FILE=$(find_section_file "*abstract*")
INTRO_FILE=$(find_section_file "*introduction*")
METHODS_FILE=$(find_section_file "*method*")
RESULTS_FILE=$(find_section_file "*result*")
DISCUSSION_FILE=$(find_section_file "*discussion*")
CONCLUSION_FILE=$(find_section_file "*conclusion*")
REFERENCES_FILE=$(find_section_file "*reference*")
APPENDIX_FILE=$(find_section_file "*appendix*")

# Count words for each section
ABSTRACT_COUNT=0
INTRO_COUNT=0
METHODS_COUNT=0
RESULTS_COUNT=0
DISCUSSION_COUNT=0
CONCLUSION_COUNT=0

[ -n "$ABSTRACT_FILE" ] && ABSTRACT_COUNT=$(count_words_in_file "$ABSTRACT_FILE")
[ -n "$INTRO_FILE" ] && INTRO_COUNT=$(count_words_in_file "$INTRO_FILE")
[ -n "$METHODS_FILE" ] && METHODS_COUNT=$(count_words_in_file "$METHODS_FILE")
[ -n "$RESULTS_FILE" ] && RESULTS_COUNT=$(count_words_in_file "$RESULTS_FILE")
[ -n "$DISCUSSION_FILE" ] && DISCUSSION_COUNT=$(count_words_in_file "$DISCUSSION_FILE")
[ -n "$CONCLUSION_FILE" ] && CONCLUSION_COUNT=$(count_words_in_file "$CONCLUSION_FILE")

# Calculate body total (excluding abstract, references, appendix)
BODY_TOTAL=$((INTRO_COUNT + METHODS_COUNT + RESULTS_COUNT + DISCUSSION_COUNT + CONCLUSION_COUNT))

# Status function
get_status() {
    local count="$1"
    local limit="$2"

    if [ "$limit" -eq 0 ]; then
        echo -e "${BLUE}--${NC}"
        return
    fi

    if [ "$count" -eq 0 ]; then
        echo -e "${YELLOW}EMPTY${NC}"
    elif [ "$count" -le "$limit" ]; then
        local pct=$((count * 100 / limit))
        echo -e "${GREEN}OK${NC} (${pct}%)"
    else
        local over=$((count - limit))
        echo -e "${RED}OVER +${over}${NC}"
    fi
}

# Get status for each section
ABSTRACT_STATUS=$(get_status "$ABSTRACT_COUNT" "$LIMIT_ABSTRACT")
INTRO_STATUS=$(get_status "$INTRO_COUNT" "$LIMIT_INTRO")
METHODS_STATUS=$(get_status "$METHODS_COUNT" "$LIMIT_METHODS")
RESULTS_STATUS=$(get_status "$RESULTS_COUNT" "$LIMIT_RESULTS")
DISCUSSION_STATUS=$(get_status "$DISCUSSION_COUNT" "$LIMIT_DISCUSSION")
CONCLUSION_STATUS=$(get_status "$CONCLUSION_COUNT" "$LIMIT_CONCLUSION")
TOTAL_STATUS=$(get_status "$BODY_TOTAL" "$LIMIT_TOTAL")

# ============================================================================
# Output
# ============================================================================

echo ""
echo -e "${BOLD}========================================================${NC}"
echo -e "${BOLD}  Word Count Report${NC}"
echo -e "${BOLD}========================================================${NC}"
echo -e "  Project:  ${BLUE}$(cd "$PROJECT_DIR" && pwd)${NC}"
echo -e "  Journal:  ${BLUE}${JOURNAL_PRESET}${NC}"
echo -e "  Date:     $(date '+%Y-%m-%d %H:%M')"
echo -e "${BOLD}========================================================${NC}"
echo ""

# Table header
printf "  ${BOLD}%-16s  %6s  %6s  %-20s${NC}\n" "Section" "Words" "Limit" "Status"
printf "  %-16s  %6s  %6s  %-20s\n" "----------------" "------" "------" "--------------------"

# Abstract (separate from body)
LIMIT_DISPLAY_ABS="$LIMIT_ABSTRACT"
[ "$LIMIT_ABSTRACT" -eq 0 ] && LIMIT_DISPLAY_ABS="--"
printf "  %-16s  %6d  %6s  " "Abstract" "$ABSTRACT_COUNT" "$LIMIT_DISPLAY_ABS"
echo -e "$ABSTRACT_STATUS"

printf "  %-16s  %6s  %6s  %-20s\n" "----------------" "------" "------" "--------------------"

# Body sections
LIMIT_DISPLAY_INTRO="$LIMIT_INTRO"
[ "$LIMIT_INTRO" -eq 0 ] && LIMIT_DISPLAY_INTRO="--"
printf "  %-16s  %6d  %6s  " "Introduction" "$INTRO_COUNT" "$LIMIT_DISPLAY_INTRO"
echo -e "$INTRO_STATUS"

LIMIT_DISPLAY_METHODS="$LIMIT_METHODS"
[ "$LIMIT_METHODS" -eq 0 ] && LIMIT_DISPLAY_METHODS="--"
printf "  %-16s  %6d  %6s  " "Methods" "$METHODS_COUNT" "$LIMIT_DISPLAY_METHODS"
echo -e "$METHODS_STATUS"

LIMIT_DISPLAY_RESULTS="$LIMIT_RESULTS"
[ "$LIMIT_RESULTS" -eq 0 ] && LIMIT_DISPLAY_RESULTS="--"
printf "  %-16s  %6d  %6s  " "Results" "$RESULTS_COUNT" "$LIMIT_DISPLAY_RESULTS"
echo -e "$RESULTS_STATUS"

LIMIT_DISPLAY_DISC="$LIMIT_DISCUSSION"
[ "$LIMIT_DISCUSSION" -eq 0 ] && LIMIT_DISPLAY_DISC="--"
printf "  %-16s  %6d  %6s  " "Discussion" "$DISCUSSION_COUNT" "$LIMIT_DISPLAY_DISC"
echo -e "$DISCUSSION_STATUS"

LIMIT_DISPLAY_CONC="$LIMIT_CONCLUSION"
[ "$LIMIT_CONCLUSION" -eq 0 ] && LIMIT_DISPLAY_CONC="--"
printf "  %-16s  %6d  %6s  " "Conclusion" "$CONCLUSION_COUNT" "$LIMIT_DISPLAY_CONC"
echo -e "$CONCLUSION_STATUS"

printf "  %-16s  %6s  %6s  %-20s\n" "----------------" "------" "------" "--------------------"

# Body total
LIMIT_DISPLAY_TOTAL="$LIMIT_TOTAL"
[ "$LIMIT_TOTAL" -eq 0 ] && LIMIT_DISPLAY_TOTAL="--"
printf "  ${BOLD}%-16s  %6d  %6s  " "BODY TOTAL" "$BODY_TOTAL" "$LIMIT_DISPLAY_TOTAL"
echo -e "${TOTAL_STATUS}${NC}"

echo ""

# Grand total including abstract
GRAND_TOTAL=$((ABSTRACT_COUNT + BODY_TOTAL))
echo -e "  Grand total (abstract + body): ${BOLD}${GRAND_TOTAL}${NC} words"
echo ""

# Warnings
if [ "$LIMIT_TOTAL" -gt 0 ] && [ "$BODY_TOTAL" -gt "$LIMIT_TOTAL" ]; then
    OVER=$((BODY_TOTAL - LIMIT_TOTAL))
    echo -e "  ${RED}WARNING: Body text exceeds journal limit by ${OVER} words.${NC}"
    echo -e "  ${YELLOW}Consider trimming the longest sections.${NC}"
    echo ""
fi

# Section balance analysis
if [ "$BODY_TOTAL" -gt 0 ]; then
    echo -e "  ${BOLD}Section balance:${NC}"
    for SECTION_NAME in "Introduction" "Methods" "Results" "Discussion" "Conclusion"; do
        case "$SECTION_NAME" in
            Introduction) COUNT=$INTRO_COUNT ;;
            Methods) COUNT=$METHODS_COUNT ;;
            Results) COUNT=$RESULTS_COUNT ;;
            Discussion) COUNT=$DISCUSSION_COUNT ;;
            Conclusion) COUNT=$CONCLUSION_COUNT ;;
        esac
        if [ "$BODY_TOTAL" -gt 0 ]; then
            PCT=$((COUNT * 100 / BODY_TOTAL))
            BAR_LEN=$((PCT / 2))
            BAR=$(printf '%0.s#' $(seq 1 $BAR_LEN 2>/dev/null) 2>/dev/null || true)
            printf "  %-14s %3d%% %s\n" "$SECTION_NAME" "$PCT" "$BAR"
        fi
    done
    echo ""
fi

# Files found/missing
echo -e "  ${BOLD}Files:${NC}"
for PAIR in \
    "Abstract:$ABSTRACT_FILE" \
    "Introduction:$INTRO_FILE" \
    "Methods:$METHODS_FILE" \
    "Results:$RESULTS_FILE" \
    "Discussion:$DISCUSSION_FILE" \
    "Conclusion:$CONCLUSION_FILE" \
    "References:$REFERENCES_FILE" \
    "Appendix:$APPENDIX_FILE"; do
    LABEL="${PAIR%%:*}"
    FILEPATH="${PAIR#*:}"
    if [ -n "$FILEPATH" ] && [ -f "$FILEPATH" ]; then
        echo -e "    ${GREEN}Found${NC}   $LABEL -> $(basename "$FILEPATH")"
    else
        echo -e "    ${YELLOW}Missing${NC} $LABEL"
    fi
done
echo ""
echo -e "${BOLD}========================================================${NC}"
echo ""
