# Figure-review HTML benchmark

Use this specification whenever generating an HTML review of Stata figures/results. The canonical visual and interaction benchmark is the project's designated reference figure-review HTML. Match its behavior and information architecture unless the user explicitly requests a different layout.

## Page structure

Use this top-to-bottom structure:

1. Small project/date metadata line.
2. Main report title.
3. Scope/method panel explaining which files were reviewed, whether values are exact or visually approximated, and how the 1–5 importance scale should be interpreted.
4. Executive-summary panel with the main empirical conclusions, contradictions, caveats, and the diagnostics that should be checked first.
5. Section navigation buttons/links, one per figure folder/group, showing the number of figures in parentheses.
6. Sticky review toolbar.
7. Figure groups in project-folder order.
8. Sequential figure cards inside each group.

## Sticky toolbar

Include all of the following controls and keep them visible while scrolling:

- Search input. Search case-insensitively across the full figure-card text, including filename, short caption, Figure meaning, Facts in the figure, Role in the paper story, Interpretation boundary, duplicate note, and source path.
- Importance filter using a minimum-score threshold: All, 5+, 4+, 3+, 2+, 1+.
- `Expand visible figures` button.
- `Collapse` button.
- Visible-count indicator in the form `visible / total`, for example `17 / 101`.

Filtering rules:

- A card is visible only when `score >= selected threshold` and the search string appears in the card text.
- Hide a figure-group heading when that group contains no visible cards.
- Update the visible-count indicator immediately after every search-input or score-filter change.
- Expand/collapse controls act only on currently visible figure cards.

## Default collapsed behavior

Each figure review must use a native `<details>` element and be **collapsed by default**. Do not set the `open` attribute during initial rendering.

Recommended structure:

```html
<details class="figure" id="fig-001" data-score="4">
  <summary>...</summary>
  <div class="body">...</div>
</details>
```

If the URL hash directly targets a figure card such as `#fig-042`, automatically open that card so cross-links to duplicate figures or diagnostics work.

## Figure numbering and summary row

- Number every file sequentially with a stable three-digit identifier: `001`, `002`, `003`, ...
- Chinese and English versions must use the same number for the same file.
- Default order: project folder order, then filename order within each folder, unless the user specifies another order.
- Keep duplicate files as separate numbered items when they exist as separate output files, but explicitly mark them as duplicates and never count them as independent evidence.

Summary-row order:

1. Importance badge such as `4/5`.
2. Three-digit figure number such as `093`.
3. Filename in monospace.
4. Short role/priority caption on a second line, e.g. `Core paper evidence`, `Important diagnostic`, `Appendix`, or `Can usually omit`.

## Expanded figure body

Use this exact vertical order:

1. `Figure meaning`
2. `Facts in the figure`
3. `Role in the paper story`
4. `Interpretation boundary`
5. Optional duplicate/relationship note with links to other figure IDs.
6. Figure image.
7. Project-relative source path at the bottom.

The four explanatory fields must appear **above the figure image**.

Use a compact two-column definition-list layout on desktop and stack it on narrow screens.

## Interpretation content

For every figure, provide all four fields. Do not leave them as generic boilerplate.

- **Figure meaning**: state the outcome, sample, grouping, time unit, denominator, and whether the plot is a stock, flow, transition, gap, or regression quantity when relevant.
- **Facts in the figure**: report the main levels, trends, gaps, reversals, support counts, or anomalies. Prefer exact values from tables/source data; clearly mark visual readings as approximate.
- **Role in the paper story**: identify whether the figure contributes to motivation, first stage, main result, health heterogeneity, mechanism, robustness, measurement validity, sample support, or background.
- **Interpretation boundary**: state what cannot be concluded from the figure and any relevant causal, sample-size, denominator, weighting, recall-window, seasonality, attrition/aging-out, measurement, right-censoring, or duplication limitations.

## Importance scale

Use the same research-value interpretation throughout the report:

- `5/5`: core paper result, core mechanism/first stage, or diagnostic essential for deciding whether the design is credible.
- `4/5`: important mechanism, robustness, support, or background evidence.
- `3/5`: useful supplementary/appendix evidence.
- `2/5`: largely redundant or peripheral; usually omit from a meeting presentation.
- `1/5`: little substantive value after validation; normally do not present.

The score is about research importance, not statistical significance or whether the figure supports the preferred hypothesis.

## Duplicate handling

When exact or near-duplicate figures exist:

- Mark the duplicate relationship in the short caption and/or an in-card note.
- Link the related three-digit figure numbers using anchors such as `#fig-007`.
- Keep each file's own source path.
- Do not describe duplicate files as separate empirical evidence.

## Image and path behavior

- Embed images in the HTML when practical so the report is self-contained.
- Use lazy loading: `loading="lazy"`.
- Show the exact project-relative path after the image in muted monospace, e.g. `figures/06_topical/hh_unmet_care_by_age_wave.png`.
- Never replace the project-relative path with a local absolute machine path in the report.

## Navigation, layout, and print

- Use section navigation links that jump to figure groups.
- Use a restrained research-report style: light neutral page background, white cards, blue/teal text accents, compact score badges, readable line height.
- Keep the main content width around the benchmark's desktop width rather than stretching full screen.
- Make the layout responsive for narrow screens.
- In print CSS, hide interactive navigation/toolbar and avoid breaking an expanded figure card across pages when possible.

## Canonical interaction script

Use behavior equivalent to:

```javascript
const cards=[...document.querySelectorAll("details.figure")];
function filter(){
  const q=document.querySelector("#q").value.toLowerCase();
  const s=+document.querySelector("#score").value;
  let n=0;
  for(const c of cards){
    const show=+c.dataset.score>=s && c.textContent.toLowerCase().includes(q);
    c.classList.toggle("hidden",!show);
    if(show)n++;
  }
  for(const g of document.querySelectorAll(".group"))
    g.classList.toggle("hidden",!g.querySelector("details:not(.hidden)"));
  document.querySelector("#count").textContent=n+" / "+cards.length;
}
function expandVisible(open){
  for(const c of cards) if(!c.classList.contains("hidden")) c.open=open;
}
document.querySelector("#q").addEventListener("input",filter);
document.querySelector("#score").addEventListener("change",filter);
function revealHash(){
  const el=document.querySelector(location.hash||"#none");
  if(el&&el.matches("details")) el.open=true;
}
window.addEventListener("hashchange",revealHash);
filter();
revealHash();
```

Keep this interaction model unless there is a specific reason to change it.

## Bilingual parity

For this project, generate both Chinese and English self-contained HTML reports by default. Keep identical:

- figure numbering;
- folder/group order;
- importance scores;
- exact numeric results;
- duplicate relationships;
- substantive conclusions and caveats;
- interaction behavior and page structure.

Translate prose, labels, captions, toolbar text, and section titles; do not alter the empirical meaning between versions.
