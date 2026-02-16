# Academic Humanizer: AI臭除去ガイド

AI が生成した学術文章から「AI臭」を除去し、人間が書いたと感じる自然な学術文章に仕上げるためのリファレンス。

出典:
- matsuikentaro1/humanizer_academic (英語18パターン)
- humanizer-ja --academic モード (日本語30パターン)
- Wikipedia: Signs of AI writing

---

## English: 18 Patterns to Detect and Fix

### Content Patterns

#### 1. Significance Inflation
AI inflates importance with vague claims about "broader impact."

| Before | After |
|--------|-------|
| represents a pivotal challenge in the evolving landscape | is highly prevalent in patients with diabetes |
| underscores the critical importance | (delete or state specific importance) |
| a key turning point / indelible mark | (delete) |

**Watch words:** pivotal, evolving landscape, underscores, highlights its importance, setting the stage for, deeply rooted, focal point, indelible mark

#### 2. Notability Claims
AI hits readers with claims of notability.

| Before | After |
|--------|-------|
| This landmark trial, led by renowned investigators | A total of 7020 patients... |

**Watch words:** landmark, renowned, prestigious, groundbreaking, impressive

#### 3. Superficial -ing Analyses
AI tacks "-ing" phrases onto sentences for fake depth.

| Before | After |
|--------|-------|
| HR 0.65, P = 0.002), highlighting the cardioprotective effects | HR 0.65; 95% CI 0.50-0.85; P = 0.002). |
| underscoring the broad applicability | The effect was consistent across subgroups. |

**Watch words:** highlighting, underscoring, emphasizing, showcasing, fostering, reflecting, contributing to

#### 4. Promotional Language
AI fails to maintain neutral academic tone.

| Before | After |
|--------|-------|
| groundbreaking study showcases the profound impact | empagliflozin reduced heart failure hospitalization |
| remarkable findings demonstrate dramatic reductions | (state the actual numbers) |

**Watch words:** groundbreaking, profound, remarkable, dramatic, stunning, breathtaking, vibrant

#### 5. Vague Attributions
AI attributes opinions to vague authorities.

| Before | After |
|--------|-------|
| Studies have shown... Experts argue... | In the EMPA-REG OUTCOME trial, empagliflozin reduced... |
| Several publications have cited | (cite the specific publications) |

**Watch words:** Studies have shown, Experts argue, Some critics, Several sources, Industry reports

#### 6. Formulaic Challenges Sections
AI produces template "challenges and future" sections.

| Before | After |
|--------|-------|
| Despite challenges... future outlook... continues to provide valuable insights | (state specific limitations factually) |

**Watch words:** Despite challenges, Despite these limitations, Future Outlook, continues to provide

### Language Patterns

#### 7. AI Vocabulary Words
Words that appear far more frequently in post-2023 AI-generated text.

**Delete or replace these:** Additionally, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate, key (adjective), landscape (abstract), pivotal, showcase, tapestry, testament, underscore (verb), valuable, vibrant

| Before | After |
|--------|-------|
| Additionally, ... a pivotal finding in the evolving therapeutic landscape | (delete "Additionally," and "pivotal" and "evolving therapeutic landscape") |
| underscoring the crucial clinical value | The number needed to treat was 35. |

#### 8. Copula Avoidance (Avoiding "is")
AI substitutes elaborate constructions for simple "is/are."

| Before | After |
|--------|-------|
| serves as the leading cause | is the leading cause |
| standing as a major clinical burden | (delete or use "is") |
| represents a significant unmet need | is an unmet need |

**Watch words:** serves as, stands as, marks, represents [a], boasts, features, offers [a]

#### 9. Negative Parallelisms
AI overuses "Not only...but..." constructions.

| Before | After |
|--------|-------|
| not only lower blood glucose but also reduce | lower blood glucose and reduce |
| This is not merely X; it is Y | (simplify) |

#### 10. Rule of Three Overuse
AI forces ideas into groups of three.

| Before | After |
|--------|-------|
| efficacy, safety, and tolerability | efficacy and safety |
| metabolic, cardiovascular, and renal domains | (use natural number of items) |

#### 11. Synonym Cycling (Elegant Variation)
AI avoids repetition by cycling synonyms, causing inconsistency.

| Before | After |
|--------|-------|
| Patients... Participants... Subjects... | Patients (consistent throughout) |
| hospitalization rates... mortality... death rates | (pick one term, use it consistently) |

#### 12. False Ranges
AI uses "from X to Y" where X and Y are not on a meaningful scale.

| Before | After |
|--------|-------|
| from improved renal function to enhanced cardiac outcomes | reduce hospitalization and improve renal outcomes |

### Style Patterns

#### 13. Em Dash Overuse
AI uses em dashes more than humans do.

| Before | After |
|--------|-------|
| benefits---a 35% reduction---appeared early | benefits (a 35% reduction) appeared early |

#### 14. Title Case in Headings
AI capitalizes all words in headings.

| Before | After |
|--------|-------|
| Statistical Analysis And Primary Endpoints | Statistical analysis and primary endpoints |

#### 15. Curly Quotation Marks
ChatGPT uses curly quotes instead of straight quotes.

### Filler and Hedging

#### 16. Filler Phrases

| Before | After |
|--------|-------|
| In order to assess | To assess |
| Due to the fact that | Because |
| It is important to note that X | X |
| At the present time | Currently (or delete) |
| With respect to | For |
| has the ability to | can |

#### 17. Excessive Hedging

| Before | After |
|--------|-------|
| may suggest that... have the potential to confer beneficial effects on | suggest that... reduce |
| in select patient populations | (state which populations, or delete) |

#### 18. Generic Positive Conclusions

| Before | After |
|--------|-------|
| The future looks bright for patients | (delete) |
| continue to reshape clinical practice | The benefit was consistent across subgroups. |
| a major step in the right direction | (delete or state specific implication) |

---

## 日本語: 学術論文向けAI臭パターン

日本語論文（である調）で特に頻出するパターン。

### A. 記号と表記

| # | パターン | Before | After |
|---|---------|--------|-------|
| 1 | emダッシュ | 多角的な視点---すなわち | 多角的な視点、つまり |
| 2 | カギ括弧で切り出しすぎ | 「真のイノベーション」とは「再構築」である | イノベーションの本質は再構築にある |
| 3 | 丸括弧で補足しすぎ | プロセス（流れ）を通じて | 流れを通じて |

### B. 文のリズム

| # | パターン | Before | After |
|---|---------|--------|-------|
| 4 | 同じ語尾が続く | である。である。である。 | である、だ、体言止めを混ぜる |
| 5 | 接続詞が多い | さらに、また、したがって | 順接の接続詞は最小限に |
| 6 | 段落の終わりが毎回きれいに閉じる | 以上がポイントである。 | 余韻を残す。閉じ方を変える |

### C. 学術文特有の問題

| # | パターン | Before | After |
|---|---------|--------|-------|
| 7 | 保険が多い（逃げ道の常設） | 一概には言えないが、一般的には有効であると考えられる | 有効である。（条件を具体的に述べる） |
| 8 | 根拠のない評価語 | 非常に有効である。大きなメリットがある | 根拠を添えるか、評価語を下げる |
| 9 | 抽象語だけで押し切る | 本質を押さえ、最適化し、価値を最大化する | 何がどうなるかを動詞中心の具体表現で |
| 10 | AIボキャブラリー（日本語版） | さらに、加えて、包括的、革新的、シームレス | 平易な日本語に置き換えるか削除 |
| 11 | 同義語の言い換え連打 | 重要・大切・欠かせない | 1回で言い切る |
| 12 | 受動態の過剰使用 | 検討が行われた。分析が実施された。 | 検討した。分析した。（能動態に） |
| 13 | 非学術的な文体の混入 | 参考になれば幸いである。ポイントは以下の通り | 削除するか、直接内容を述べる |

### D. 日本語AIボキャブラリー一覧

以下の語が高密度で出現している場合、AI生成を疑う：

さらに / また / 加えて / 包括的 / 革新的 / シームレス / 多角的 / 本質的 / 不可欠 / 重要な役割を果たす / 大きな意義を持つ / 注目に値する / 示唆に富む / 興味深いことに / 特筆すべきは

---

## Section-Specific Application

各セクションでの重点チェック：

| Section | 重点パターン | 理由 |
|---------|-------------|------|
| Introduction | #1 Significance inflation, #5 Vague attributions | 背景を膨らませがち |
| Methods | #16 Filler phrases, #8 Copula avoidance | 冗長になりがち |
| Results | #3 -ing analyses, #4 Promotional language | 結果に解釈を混ぜがち |
| Discussion | #17 Excessive hedging, #6 Formulaic challenges | 考察が定型化しがち |
| Conclusion | #18 Generic conclusions, #1 Significance inflation | 締めが空疎になりがち |
| Abstract | All patterns | 最も目に触れる部分 |

---

## Quick Checklist (Before Submission)

### English
- [ ] No "Additionally" / "Furthermore" at sentence start (> 2 times)
- [ ] No "pivotal" / "crucial" / "landscape" / "delve"
- [ ] No "-ing" phrases tacked on for fake depth
- [ ] No "serves as" / "stands as" (use "is")
- [ ] No vague "Studies have shown" (cite specific study)
- [ ] No generic positive conclusion
- [ ] Consistent terminology (not synonym cycling)
- [ ] Em dashes used sparingly (< 2 per page)
- [ ] Hedging is proportionate to evidence

### 日本語
- [ ] 「さらに」「また」「加えて」の連発がない
- [ ] 同じ語尾が3回以上続いていない
- [ ] 根拠なき「非常に」「大きな」がない
- [ ] 受動態の過剰使用がない（能動態に直す）
- [ ] 定型的な締めの句がない
- [ ] 抽象語だけで押し切っていない
- [ ] カギ括弧を多用していない

---

## References

- Wikipedia: Signs of AI writing
- matsuikentaro1/humanizer_academic (English academic patterns)
- humanizer-ja (Japanese patterns, --academic mode)
- Fitchett D, et al. Circulation. 2019;139(11):1384-1395. (Example source, CC-BY-4.0)

---

## 日本語: セクション別重点パターン

各セクションで特に注意すべきパターン。全パターンのチェックは必須だが、以下のパターンは各セクションで特に頻出する。

| セクション | 重点パターン | 理由 |
|-----------|-------------|------|
| 緒言 | C-2 根拠なき評価語, B-2 接続詞過多 | 背景を膨らませがち |
| 方法 | C-6 受動態の過剰使用, C-3 抽象語 | 冗長になりがち |
| 結果 | B-1 同じ語尾, A-3 丸括弧多用 | 単調になりがち |
| 考察 | C-1 保険が多い, C-4 AIボキャブラリー | 考察が定型化しがち |
| 結論 | C-2 根拠なき評価語, C-7 非学術的文体 | 締めが空疎になりがち |
| 抄録 | 全パターン | 最も目に触れる部分 |

### C-7: 非学術的な文体の混入（追加パターン）

AIが学術論文にブログ・SNS・FAQ調の文体を混入させるパターン。

| Before | After |
|--------|-------|
| 参考になれば幸いである | （削除） |
| ポイントは以下の通りである | （削除し、直接内容を述べる） |
| まずは小さく始めてみてはいかがだろうか | （削除） |
| 以上が本研究のポイントである | 本研究の結果は以下の通りである |
| 興味深いことに | （削除、または具体的な理由を述べる） |

このパターンはLLMの学習データにFAQ・ブログ・研修資料が多く含まれるために発生する。学術論文では読者への語りかけや感想表現を避ける。
