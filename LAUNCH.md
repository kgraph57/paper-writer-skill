# Launch Kit — paper-writer-skill

Use this file to announce the GitHub Pages landing and Week 1 packaging without rewriting copy from scratch.

## Launch Goal

Put the skill in front of clinicians, clinician-scientists, and agent users who write medical/scientific manuscripts — and who care that IDEA/DATA stay human.

Primary outcomes: GitHub stars, installs via `npx skills add`, forks, saves, thoughtful replies, inbound case-study requests.

**Do not invent metrics** (user counts, acceptance rates, journal names of "wins").

## Links to include everywhere

- Live landing: https://kgraph57.github.io/paper-writer-skill/
- Case study (2-minute read): https://github.com/kgraph57/paper-writer-skill/blob/main/examples/case-studies/discovery-to-draft.md
- Repo: https://github.com/kgraph57/paper-writer-skill
- Install: `npx skills add kgraph57/paper-writer-skill`

## Release Copy (Week 1 / v3.2 packaging)

Lead with: research engine ≠ manuscript factory → Discovery gates → humanizer → adversarial review → install + star.

### X / Twitter (JP) — primary

```text
原稿工場じゃなく、研究エンジン。

paper-writer-skill（Claude Code / エージェント用）:
- Phase −1 Discoveryで質問を鍛え、💡IDEA と 📊DATA は人間がロック
- ステージゲート付きIMRAD（FAILなら自動修正ループ）
- 日英ヒューマナイズ（学術AIパターン除去）
- 敵対的レビューが弱い主張をKILLできる

紹介サイト: https://kgraph57.github.io/paper-writer-skill/
ケース（2分）: https://github.com/kgraph57/paper-writer-skill/blob/main/examples/case-studies/discovery-to-draft.md
Install: npx skills add kgraph57/paper-writer-skill
★ Starもらえると助かります
```

### X / Twitter (EN)

```text
Not a manuscript factory. A research engine.

paper-writer-skill for Claude Code / agents:
- Phase −1 Discovery forges questions; humans lock 💡 IDEA and 📊 DATA
- Stage-gated IMRAD with auto-fix loops on FAIL
- EN+JP academic humanizer (AI-tell patterns)
- Adversarial review that can KILL a weak claim before submission

Landing: https://kgraph57.github.io/paper-writer-skill/
Case study (2 min): https://github.com/kgraph57/paper-writer-skill/blob/main/examples/case-studies/discovery-to-draft.md
Install: npx skills add kgraph57/paper-writer-skill
★ Star if this is the manuscript workflow you wanted
```

### Show HN (Hacker News)

```text
Title: Show HN: Agent skill for medical manuscripts – discovery gates, humanizer, adversarial review

I packaged my Claude Code / agent skill for medical and scientific
writing with a public landing page and a 2-minute case study.

It is intentionally not a "paste notes → camera-ready PDF" factory.
Phase −1 Discovery forges and ranks research questions, checks novelty
against live literature, and stops until a human locks the 💡 IDEA and
confirms 📊 DATA (real, never model-invented). Drafting then runs through
stage-gates with auto-fix loops, an EN+JP academic humanizer, citation
checks, and an adversarial review that can KILL a weak central claim
before any journal sees it.

Six paper types (original, case report, review, SR, letter, protocol),
20+ reporting guidelines, team mode with parallel agents, and tested
Python utilities (table1, SR helpers). Network is used for literature
APIs — not telemetry. Raw clinical data stays local / gitignored.

Landing: https://kgraph57.github.io/paper-writer-skill/
Case study: https://github.com/kgraph57/paper-writer-skill/blob/main/examples/case-studies/discovery-to-draft.md
Install: npx skills add kgraph57/paper-writer-skill
Repo: https://github.com/kgraph57/paper-writer-skill
```

### LinkedIn (short, optional)

```text
Shipping a public intro site for paper-writer-skill — an agent skill for medical/scientific manuscripts.

Thesis: research engine ≠ manuscript factory. Humans stay sovereign on IDEA and DATA; the agent runs discovery, stage-gated IMRAD, EN+JP humanizing, and adversarial review.

Landing: https://kgraph57.github.io/paper-writer-skill/
Install: npx skills add kgraph57/paper-writer-skill
```

### Reddit (optional — tone check before posting)

Good fits when the community allows tool shares: r/ClaudeAI, r/LocalLLaMA (agent workflows), academic writing communities that accept OSS tool posts. Lead with the case study + sovereignty gates; avoid hype and medical advice. Do not spam.

```text
I open-sourced an agent skill (SKILL.md) for medical manuscript workflows: discovery gates before drafting, stage-gates, EN+JP humanizer, adversarial review. Humans lock IDEA/DATA. Landing + 2-min case study in the links. Not affiliated with any journal. Feedback welcome on the discovery → kill-path design.
```

## Checklist before posting

- [ ] GitHub Pages live at `/docs` on `main` (see `POST_MERGE.md`)
- [ ] Repo `homepage` set to the Pages URL
- [ ] Case study link returns 200
- [ ] LICENSE is MIT (not "Private repository" in README)
- [ ] Topics include `claude-skills`, `claude-code-skill`, `agent-skills`
