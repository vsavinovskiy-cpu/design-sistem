---
name: design-system
description: Builds and reviews design systems. Use when working with tokens, components, naming, typography, icons, or governance.
allowed-tools: Read, Write, Edit, Glob, mcp__pencil__batch_get, mcp__pencil__batch_design, mcp__pencil__get_guidelines, mcp__pencil__get_variables, mcp__pencil__set_variables
---

# Design System

## Token Architecture

1. Build three layers: primitive → semantic → component
2. Primitives: raw values (e.g. `color.blue.500 = #3B82F6`)
3. Semantic: intent-based aliases (e.g. `color.action.primary = {color.blue.500}`)
4. Component: scoped overrides (e.g. `button.bg.default = {color.action.primary}`)
5. Export tokens as JSON for cross-platform use (iOS, Android, Web)
6. Use Token Studio or native Figma variables for theme switching

## Color

1. Define a full primitive palette per hue (50–950 steps)
2. Map semantic aliases: background, foreground, border, action, status
3. Create separate light/dark theme variable sets
4. Semantic tokens reference primitives — never hardcode hex at semantic level

## Typography

1. Define a type scale as tokens: size, line-height, weight, tracking
2. Set explicit line-height — do not rely on auto
3. Create named text styles from token combinations (e.g. `heading/xl`, `body/md`)
4. Use monospace-friendly fonts where code display is needed (check 0/O ambiguity)

## Components

1. Name by function, not appearance (`select` not `dropdown-menu`)
2. Define variants for all interactive states: default, hover, active, disabled, error
3. Avoid deep atom nesting — prefer flat structure with fewer hidden layers
4. Use min-width/min-height to reduce wrapper containers
5. Separate base components from product-specific ones
6. Test new components locally before proposing to the library

## Icons

1. Store as outlines only, single color, single size
2. Use `scale` constraints on internals
3. Keep stroke-based icons on a separate page for editability
4. Export as SVG

## Spacing & Grid

1. Define spacing scale as tokens (base unit × multiplier)
2. Fixed gap between headings — prevents layout gaps
3. Grid: columns, gutter, margin as named tokens per breakpoint

## Naming Conventions

1. Use consistent taxonomy: `category/variant/state` (e.g. `button/primary/hover`)
2. Agree on a single term per concept across the team before building
3. Document naming decisions — avoid synonym drift over time

## Governance

1. Maintain a core team as the gatekeeper for library changes
2. Designers contribute via branches — review before merging to main library
3. Local libraries + swap library mechanism for testing before promotion
4. Version the library; communicate breaking changes explicitly
5. Track component usage analytics (Figma Enterprise analytics or plugin)

## Rules

- One source of truth: tokens in one place, consumed everywhere
- No hardcoded values inside components — always reference a token
- Every new component requires: defined states, token coverage, naming decision
- Avoid premature abstraction — three similar components before extracting a base
