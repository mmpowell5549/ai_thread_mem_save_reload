markdown
~~This text will be crossed out.~~Here's the complete Markdown reference guide as a single copy-pasteable file. Select everything inside the code block below and paste it into a new file named markdown-cheatsheet.md.

markdown
# Markdown Reference Guide created by Grok AI
**Quick-search + copy-paste reference**  
Covers **CommonMark** (standard) + **GitHub Flavored Markdown (GFM)** extensions.  
Most modern editors, GitHub, GitLab, VS Code, Obsidian, etc. support both.

---

## Table of Contents
- [Quick Lookup](#quick-lookup)
- [Headings](#headings)
- [Text Formatting](#text-formatting)
- [Lists](#lists)
- [Links](#links)
- [Images](#images)
- [Code](#code)
- [Blockquotes](#blockquotes)
- [Tables](#tables)
- [Horizontal Rule](#horizontal-rule)
- [Line Breaks & Paragraphs](#line-breaks--paragraphs)
- [Task Lists](#task-lists)
- [Footnotes](#footnotes)
- [Escaping](#escaping)
- [HTML](#html)
- [Math (optional)](#math-optional)
- [Common Gotchas](#common-gotchas)

---

## Quick Lookup

| Element              | Syntax                          | Notes                  |
|----------------------|---------------------------------|------------------------|
| H1                   | `# Heading`                     | Space after # required |
| Bold                 | `**bold**` or `__bold__`        | Prefer `**`            |
| Italic               | `*italic*` or `_italic_`        | Prefer `*`             |
| Bold + Italic        | `***both***`                    |                        |
| Strikethrough        | `~~text~~`                      | GFM                    |
| Inline code          | `` `code` ``                    |                        |
| Code block           | ```` ```lang ````               | Triple backticks       |
| Link                 | `[text](url)`                   |                        |
| Image                | `![alt](url)`                   |                        |
| Unordered list       | `- item`                        | Also `*` or `+`        |
| Ordered list         | `1. item`                       |                        |
| Task list            | `- [ ]` / `- [x]`               | GFM                    |
| Table                | `\| A \| B \|` + `\| --- \| --- \|` | GFM               |
| Blockquote           | `> quote`                       |                        |
| Horizontal rule      | `---`                           | Also `***` or `___`    |
| Line break           | Two trailing spaces or `\`      |                        |
| Footnote             | `[^1]` + `[^1]: note`           | GFM                    |
| Escape               | `\*` or `\#` etc.               |                        |

---

## Headings

```markdown
# H1
## H2
### H3
#### H4
##### H5
###### H6
Alternative (H1 & H2 only):

markdown
H1 Title
========

H2 Title
--------
Tip: Always put a space after the #. Use one H1 per document.

Text Formatting
markdown
**bold**
__bold__

*italic*
_italic_

***bold italic***
___bold italic___

~~strikethrough~~          <!-- GFM -->

`inline code`

**Bold with *italic* inside**
*Italic with **bold** inside*
Lists
Unordered
markdown
- Item
- Item
  - Nested (2–4 spaces)
  - Nested
- Item
Also works with * or +.

Ordered
markdown
1. First
2. Second
   1. Nested
   2. Nested
3. Third
Actual numbers don't matter for rendering (most processors renumber).

Mixed / Complex
markdown
1. Ordered
   - Unordered nested
   - Another
2. Back to ordered
Links
markdown
[Inline link](https://example.com)
[Link with title](https://example.com "Hover title")

[Reference link][id]
[id]: https://example.com "Optional title"

<https://example.com>           <!-- Autolink -->
<user@example.com>              <!-- Email autolink -->
Images
markdown
![Alt text](https://example.com/image.png)
![Alt text](image.png "Optional title")

[![Clickable image](image.png)](https://example.com)
Code
Inline
markdown
Use `backticks` for inline code.
Use `` `double` `` if you need a backtick inside.
Fenced block (preferred)
markdown
```javascript
function hello() {
  console.log("Hello");
}
```
markdown
```python
print("Hello")
```
Indented block (4 spaces)
markdown
    This is indented code
    (no language highlighting)
Blockquotes
markdown
> This is a blockquote.
>
> It can span multiple lines.
>
> > Nested quote.
Tables
GFM only

markdown
| Left   | Center | Right  |
| :----- | :----: | -----: |
| a      | b      | c      |
| d      | e      | f      |
--- = left-aligned (default)
:--- = left
:---: = center
---: = right
Horizontal Rule
markdown
---
***
___
(Must be alone on the line; add blank lines around it for safety.)

Line Breaks & Paragraphs
markdown
This is a paragraph.
This is still the same paragraph (soft break).

This is a new paragraph (blank line required).

Hard line break: end line with two spaces  
or with a backslash\
then continue.
Task Lists
GFM

markdown
- [ ] Unchecked
- [x] Checked
- [ ] Nested
  - [x] Also works
Footnotes
GFM

markdown
Here is a footnote reference[^1].

[^1]: This is the footnote text.
Escaping
Escape special characters with \:

markdown
\*not italic\*
\# not a heading
\[not a link\]
\`not code\`
Common characters to escape: \ * _ { } [ ] ( ) # + - . ! | `

HTML
Markdown allows raw HTML (most processors):

markdown
<u>Underline</u>
<mark>Highlight</mark>
<sup>Superscript</sup>
<sub>Subscript</sub>
<br>   <!-- line break -->

<!-- HTML comment (ignored) -->
Math (optional)
Supported in many modern renderers (GitHub, Obsidian, Typora, etc.):

markdown
Inline: $E = mc^2$

Block:
$$
\int_a^b f(x)\,dx
$$
Common Gotchas
Space after # is required for headings.
Blank lines are important between blocks.
Nested lists need consistent indentation (usually 2 or 4 spaces).
Tables must have a header separator row.
Trailing spaces for line breaks are invisible — prefer \ or <br>.
Most processors are lenient; strict CommonMark is stricter than GitHub.
Last updated: 2026
Save this file and use your editor’s search (Ctrl/Cmd+F) for instant lookup.

