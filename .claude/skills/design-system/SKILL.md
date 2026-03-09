---
name: design-system
description: Builds and reviews design systems. Use when working with tokens, components, naming, typography, icons, or governance.
allowed-tools: Read, Write, Edit, Glob, Grep, mcp__pencil__batch_get, mcp__pencil__batch_design, mcp__pencil__get_guidelines, mcp__pencil__get_variables, mcp__pencil__set_variables
---

# Design System

## Diagnose First

Before proposing anything, read existing tokens and ask:

- How many token layers? (2, 3, or 4)
- What token format? (Token Studio JSON / W3C $type-$value / Style Dictionary / Figma Variables)
- What color format? (HEX / HSL / oklch / RGB)
- What palette step model?
- What semantic color model?
- How is dark mode handled?
- What spacing model?

## Token Architecture

**2-layer** `primitive → semantic` — simpler, fewer tokens, less flexible (Radix, Tailwind)
**3-layer** `core → semantic → component` — standard for large systems (Carbon, Material)
**4-layer** `core → semantic → component → product` — multi-brand enterprise systems

Token formats vary:
- Token Studio: `{reference}` syntax, supports math expressions (`{base} * 4`)
- W3C standard: `$type` / `$value` fields
- Figma Variables: native, no math, mode-based

**Always true regardless of approach:**
- Semantic tokens reference primitives — never hardcode at semantic level
- Component tokens reference semantic — never skip layers
- One source of truth per token

## Color

**Palette steps:**
- Material: 50–900 (10 steps) — widely known, weak at extremes
- Tailwind: 50–950 (11 steps) — better dark coverage
- Custom 0–1000 (12 steps) — full control, more decisions required
- Radix 1–12 — semantic meaning baked into step number

**Alpha/transparency:**
- Explicit alpha scale per color (e.g. 4/8/12/16/24/32/40%) — verbose, predictable
- CSS opacity modifier — fewer tokens, runtime only
- Opaque tinted alternatives — no compositing issues, harder to maintain

**Semantic color models:**
- Role-based: `surface / text / border / icon` (Carbon)
- Intent-based: `primary / brand / success / warning / critical / info / draft`
- Context-based: `background / foreground / accent` (Radix)

**Dark mode:**
- Separate semantic sets per theme — explicit, most tokens, easiest to reason about
- Single set with CSS inversion — fewer tokens, breaks for complex palettes
- CSS `color-scheme` + relative colors — fewest tokens, requires modern browser support

## Typography

**Scale models:**
- Modular (ratio-based: 1.25×, 1.333×) — mathematically consistent, less control
- Custom numeric (e.g. 100–900) — precise, requires manual decisions
- T-shirt sizes (xs–xl) — readable, imprecise

**Line height:**
- Ratio to font size (1.5×) — simple
- Base-unit snapping (nearest multiple of 4px) — grid-aligned
- Tight / paragraph variants per size — explicit, good for components and prose separately

**Text style naming:**
- By role: `display / headline / body / caption / label`
- By size: `text-xl / text-lg`
- Combined: `heading/xl`, `body/md/regular`

## Spacing

**Models:**
- Base-unit multiples (`space = base × N`) — predictable, dense scale
- T-shirt semantic aliases (`xs/sm/md/lg/xl`) — readable, maps to multiples underneath
- Typography-derived (spacing tied to line-height) — text-rhythm consistency
- Static named steps (`x1…x20`) — explicit, no abstraction

Many systems layer these: semantic aliases map to static steps.

## Components

**State coverage:**
- Minimum: default, hover, active, disabled, error
- Extended: + focus, loading, readonly, empty, skeleton

**Surface patterns:**
- filled / outlined / toned / ghost / transparent — per semantic color category
- Elevation levels (elevation0, elevation1…) — for layered surfaces with depth

**Naming:** always by function (`select`, `dialog`) — never by appearance (`blue-button`, `dropdown-menu`)

## Working with .pen Files

When task involves .pen files:
1. Call `mcp__pencil__get_editor_state` — identify active file and selection
2. Call `mcp__pencil__get_guidelines` with topic `design-system` — before any design work
3. Call `mcp__pencil__get_variables` — check existing tokens/variables in the file
4. Call `mcp__pencil__batch_get` — read existing nodes before modifying
5. Call `mcp__pencil__batch_design` — apply changes
6. Call `mcp__pencil__get_screenshot` — validate result visually

When creating or updating variables: use `mcp__pencil__set_variables`.

## Rules

- No hardcoded values inside components — always reference a token
- Every new component needs: states defined, tokens assigned, name agreed
- When approach is unclear — read existing tokens before proposing anything
- Avoid premature abstraction — three similar components before extracting a base
