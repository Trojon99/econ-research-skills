# Research learning behavior checks

[The case set](learning-workflow-cases.json) contains synthetic requests and expected reasoning, not fabricated empirical results. These are manually reviewed regression fixtures. Their presence, JSON validity or package test success does not mean an assistant passed them.

## Run a behavior check

1. Select the skill revision and case IDs before evaluation. Record runtime model/provider, available tools, installed public/local differences and evaluator identity. Do not use private source corpora as public fixtures.
2. Send the exact case prompt to a fresh evaluation session with the relevant entrypoint and references available. Do not supply `expected` or `failures` as part of the tested prompt. Retain actual output and invoked references locally.
3. Review the output against every expected element and prohibited failure. Mark each element satisfied, failed or not assessable with a quotation/evidence. Judge reasoning and scope, not keyword frequency. Ambiguous cases need a second reviewer.
4. Record pass only if required elements are met and no consequential failure remains. Distinguish an unavailable retrieval/tool from an invented successful result. Do not award a pass from an evaluator's unsupported summary.
5. Compare revisions on the same case/environment when meaningful. These cases are small and hand-designed: passing does not certify all economic advice or real-world research performance.

Keep evaluation answers and scorecards outside the public repository by default. A compact scorecard should contain case ID, skill commit, runtime, exact prompt, response artifact, criterion-by-criterion findings, evaluator, verdict and limitations. CI runs packaging and ledger integrity tests only; there is no hidden LLM evaluator or external paid API call.

## Extend the set

Add a case when a real task exposes a consequential error. Generalize away private data and publication-sensitive details, preserve the hard reasoning distinction, and add a competing interpretation when necessary. Update the rubric after substantive methodological review, not merely to make the current assistant pass. Numerical/code checks belong in executable tests and should be reported separately.
