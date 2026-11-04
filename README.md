# Coding Agents 101: Workflows & Best Practices

A LaTeX Beamer talk on delegating research-code tasks to coding agents. It covers what a request needs; an environment with conda or uv and automatic checks with Ruff, mypy and Pylance; how a prepared repository (a standard layout, `AGENTS.md`, `GLOSSARY.md`, `CODING_STANDARDS.md`, ADRs) lets the request stay short; version control with git, with worktrees for parallel agents and for a session forked in two; working test-first; skills, from the idea to Matt Pocock's collection, the classic books it draws on and an example `/grill-with-docs` session; and other skill packages that also set the check before the code, with a checklist for your own repository. One running example carries the talk: splitting a segmentation dataset by specimen. An appendix holds templates, tool details and references.

## Start here

- [Audience PDF](presentation/build/main.pdf): 57 pages, 47 for the 46 talk slides (slide 5 builds up in two steps) and 10 appendix pages.
- [Speaker notes](presentation/build/speaker-notes.pdf): 45 pages: one per talk slide (dividers excluded) with the slide image, notes and timing; after slide 29, five pages with the "Why These Skills Exist" section of Pocock's README; and one for each of the two backup slides on uv in the appendix (A3, A4).
- [Timed outline](OUTLINE.md) and [sources and provenance](SOURCES.md).

## Files

| Path | Content |
|---|---|
| `presentation/main.tex` | Entry point: title, presenter, date, section files |
| `presentation/beamerthemed3m.sty` | Theme: UdS colours, fonts, mini-frame headline, footer, blocks, code boxes |
| `presentation/slides/*.tex` | One file per section; `09-appendix.tex` holds the appendix |
| `presentation/assets/` | UdS logo (vector), d3M logo, HCCI micrographs with `provenance.csv`, screenshots in `screens/` |
| `presentation/tools/prepare_hcci_images.py` | Re-creates the HCCI micrographs, cropped or full frame, and the mask from the dataset |
| `presentation/build.ps1` | Build script (XeLaTeX, three passes) |

`THIRD-PARTY-NOTICES.md` lists the material by others in the slides and notes, with its licence: the HCCI micrographs (CC BY 4.0), the excerpts of Matt Pocock's skills (MIT), the two logos and the screenshots.

## Build

From the `presentation` folder in PowerShell:

```powershell
.\build.ps1
.\build.ps1 speaker-notes
```

Requirements: XeLaTeX (tested with MiKTeX) with beamer, TikZ, tcolorbox, listings and fontawesome5. Text is set in Latin Modern Sans, the OpenType version of Computer Modern Sans that ships with TeX. Code uses [FiraCode Nerd Font Mono](https://www.nerdfonts.com/font-downloads), which must be installed on the system; without it the theme falls back to Latin Modern Mono. Three passes are needed because the title page and section dividers place their graphics relative to the page. On Overleaf, select XeLaTeX and upload the FiraCode Nerd Font files, or rely on the fallback; the included `.latexmkrc` lets latexmk repeat passes as needed.

## Editing

- Title, presenter and date: `\title{}`, `\subtitle{}`, `\author{}` and `\date{}` in `main.tex`, with the PDF's own title and author in its `\hypersetup`. The title slide shows the presenter under the subtitle and the date at the bottom.
- Citations: the frame option `source={...}` prints a short citation in the footer, for example `source={Beck (2002), Test-Driven Development: By Example}`. Full references go on slides A7 to A10.
- Section dividers: `\sectionframe{number}{title}{question}{icon}`, where the icon is a fontawesome5 command such as `\faCodeBranch` or `\faIcon{shield-alt}`.
- Boxes: `dblock` (blue, information), `ablock` (red, decisions and warnings), `fblock` (dark, files), `gblock` (green, passing tests), `panel` (untitled), `codefile` (a file's contents, shown as in an editor: a tab with an icon and the path, such as `docs/adr/0003-specimen-level-splits.md`, above a white page; Markdown by default, `[style=sh]` greys `#` comments for shell, TOML, YAML and `.gitignore`, `[style=py]` for Python), `terminal` (commands shown in a terminal window: dark, three dots and a centred title; `$` prompts green, `#` comments grey, `§\textcolor{termred}{...}§` or `termgreen` for output), `terminalwindow` (the same frame around a terminal screenshot), `foldertree` (a folder structure on a white page with the file window's border: `\tdir{depth}{name}{note}` and `\tfile{depth}{name}{note}` rows with blue folder and grey file icons, guides drawn to each parent, notes at `note at=`; `\tbadge{style}{text}` adds a badge at `badge at=`, `\tstrike` strikes a name; `\tdirgrey` and `\tfilegrey` draw rows in grey, for parts left as they were). To join a tree to other drawings with arrows, as on slide 10, draw its rows inside the slide's own `tikzpicture[x=1mm,y=1mm]`: `\treestart{note at=..,row height=..}` in a shifted scope starts the rows at y = 0, and the white page is drawn around them.
- Task specification cards, inside a `tikzpicture[x=1mm,y=1mm]` (slides 4, 5, 16 and 17; slide 16 draws them in grey by redefining `udsblue` and `udsdark` with `\colorlet` inside a group): `\specterminal{y top}{title}` draws the request as a terminal across the text width, set in `[spec request]` nodes; `\speccard{k}{y top}{y bottom}{label}{body fill}` draws card `k` (0 to 4) of objective, context, constraints, acceptance and verification at fixed positions; `\specfilecard` gives the card a dark head and a file icon, for a part that comes from files; `spec chip`, `spec skill` and `spec note` fill a card with file names, skills and notes.
- Tables: booktabs rules; `>{\columncolor{redtint}}` tints a column (colortbl), and with `\aboverulesep` and `\belowrulesep` at 0pt the tint meets the rules.
- Colour carries meaning in the diagrams (blue: agent or tool, red: person, decision or held-out data, dark: files and the parts of a task that come from files, green: passing tests), and every element also has a text label.
- Screenshots: `SOURCES.md` describes how each one in `presentation/assets/screens/` was made, so it can be retaken. Number what the audience should look at with `\node[number mark] at (x,y) {1};` and repeat the marker in the text with `\numbermark{1}`, for example as the label of the item it numbers, `\item[\numbermark{1}]`, as on slides 8 and 23.
- Speaker notes: `\note{\textbf{12:50--13:50}\par First point.\par Second point.}`, the time range first, then one sentence per line, so the notes pages work as cues. A backup slide in the appendix starts its note with `\textbf{If asked}` instead of a time range, so it adds nothing to the talk's length. A slide that builds up in steps, such as slide 5 with `\only<2->{...}`, attaches its note to the last step, `\note<2>{...}`, so the notes show it once, with the whole slide. A `\note{...}` outside any frame makes a notes page of its own after the previous slide's, as for the README pages after slide 29; it starts with `\parindent=0pt\parskip=1.1mm\raggedright`, the style frame notes get from the theme. The title slide is drawn inside its frame, not over the page, so that its notes page shows it too; the closing slide repeats its layout, with the blue panel drawn by `\titlepanel` from `00-title.tex`.
- Text size: anything the audience must read, code included, is at least 7 pt. Screenshots stay smaller, so their caption or a numbered marker carries the message. A term the audience may not know (pull request, mock, seam) is explained in the speaker notes where it first appears.
- Spacing: the theme starts every slide's content 4 mm below the title, whether it begins with text, a list, a block, a table or an image, and in `[T]` columns both columns start on the same line. Do not add `\vspace` at the start of a frame or use the `[c]` frame option; a tcolorbox raster needs `raster before skip=0pt`.
