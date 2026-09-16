# HTML Results Report Layout

Use this reference whenever producing an HTML results interpretation or showcase report.

## Persistent report navigation pattern

Place one compact navigation card immediately below the hero/header and before the first substantive content block. Treat this row as a standard part of the report, not an optional decoration.

On desktop, keep the row horizontal:

- left side: section links;
- right side: a search field aligned at the far end of the same row.

Use simple text links rather than large pill buttons. Match the established report visual language: white rounded card, light border, restrained shadow, generous horizontal padding, blue/dark-blue link text, and substantial whitespace.

Do not make the navigation sticky unless the user explicitly asks for sticky behavior.

## Section links

Use this default order and keep the wording matched to the report language.

Chinese report:

1. `摘要`
2. `图`
3. `表`
4. `解释范围`
5. `综合叙事`

English report:

1. `Summary`
2. `Figures`
3. `Tables`
4. `Interpretation Scope`
5. `Overall Story`

Each link must point to a real section anchor in the same document. Use stable semantic IDs such as:

- `#summary`
- `#figures`
- `#tables`
- `#interpretation-scope`
- `#overall-story`

If a report genuinely omits one of these sections, omit the corresponding link rather than linking to an empty anchor.

## Search field

Add a functional client-side search input at the far right of the navigation row.

Recommended placeholders:

- Chinese: `搜索图表、关键词或结果…`
- English: `Search figures, tables, or results…`

Search behavior:

- search case-insensitively across figure titles, table titles, item interpretations, and the synthesis text;
- update results as the user types;
- highlight matched terms when practical;
- hide or de-emphasize nonmatching figure/table cards rather than navigating away from the page;
- preserve section headings so the report structure remains understandable while filtering;
- show a small neutral `No matching results` / `没有匹配结果` message when nothing matches;
- clearing the input restores the complete report;
- pressing `Escape` should clear the search when simple inline JavaScript is used;
- use no external JavaScript dependency for this behavior.

The search is a report-navigation aid, not a data-analysis feature. It must never alter numbers, figure images, table contents, or substantive interpretations.

## Recommended HTML structure

A compact implementation can follow this pattern:

```html
<nav class="report-nav" aria-label="Report sections">
  <div class="report-nav-links">
    <a href="#summary">摘要</a>
    <a href="#figures">图</a>
    <a href="#tables">表</a>
    <a href="#interpretation-scope">解释范围</a>
    <a href="#overall-story">综合叙事</a>
  </div>
  <div class="report-search">
    <input id="report-search-input" type="search"
           placeholder="搜索图表、关键词或结果…"
           aria-label="搜索报告内容">
  </div>
</nav>
```

The English version should use the English link labels and placeholder while retaining the same structure.

Mark searchable figure/table/result blocks with a shared selector such as `.report-item`. Keep section-level synthesis blocks searchable as well when useful.

## Responsive behavior

On wide screens:

- keep links on the left and the search field on the far right;
- keep the search box visually subordinate to the navigation links;
- a search width around 240–320px is usually sufficient.

On narrow screens:

- allow the navigation row to wrap cleanly;
- let the search field move to a second line and expand to the available width;
- do not shrink link text until it becomes difficult to tap or read;
- preserve the same section order.

## Visual consistency

The navigation card should visually match the report rather than resemble a website application toolbar. Prefer:

- rounded corners consistent with the main content cards;
- white or the report's card background;
- a subtle border and shadow;
- compact link spacing;
- restrained focus states on links and search input;
- no oversized icons, gradients, or decorative controls unless the rest of the report already uses them.

If the user provides a screenshot or an existing HTML report as a visual reference, preserve that navigation-row composition and add the search field to the far right without redesigning the rest of the row.
