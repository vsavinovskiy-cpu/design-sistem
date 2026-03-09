---
name: midjourney
description: Write and improve Midjourney prompts. Trigger when user asks to create, write, or improve a Midjourney image prompt.
allowed-tools: WebSearch
---

# Midjourney Prompt Writer

## Workflow

1. Clarify intent if vague (subject, style, mood)
2. Build prompt using dimensions below
3. Select appropriate parameters
4. Output the final prompt in a code block
5. Briefly explain key choices

## Prompt Structure

```
[subject], [medium], [environment], [lighting], [color], [mood], [composition] --param value
```

**Short phrases beat long sentences.** Midjourney reads descriptors, not instructions.

### Dimensions

| Dimension | Examples |
|-----------|---------|
| Subject | person, animal, object, landscape |
| Medium | photo, oil painting, watercolor, pencil sketch, ukiyo-e, risograph, pixel art, cyanotype, block print |
| Environment | forest, city, ocean, cave, tundra, salt flat, crystal forest |
| Lighting | soft, neon, studio, overcast, ambient, golden hour |
| Color | vibrant, pastel, duotone, grayscale, iridescent, neon, sepia |
| Mood | playful, calm, gloomy, energetic, determined, joyful |
| Composition | closeup, portrait, bird's-eye view, headshot, wide angle |

### Vocabulary Tips

- Specific synonyms: "gigantic" > "big", "crimson" > "red"
- Specific numbers: "three cats" > "cats"
- Collective nouns: "flock of birds" > "birds"
- Describe what you WANT — use `--no` for exclusions

## Core Parameters

```
--ar W:H      aspect ratio (default 1:1). No decimals. Use: 16:9, 9:16, 4:3, 2:3, 1:1
--s 0-1000    stylize (default 100). Higher = more artistic. Lower = more literal.
--c 0-100     chaos (default 0). Higher = more variety between the 4 images.
--w 0-3000    weird. Quirky/unconventional. V6/V7 only.
--q 1|2|4     quality (default 1). Higher = more GPU time, more detail.
--no item     exclude elements. Specific items only — each word read independently!
--seed #      reproducibility (0–4294967295). Same seed → similar results.
--v 6|6.1|7   model version (default V7)
--niji 6      anime model
--raw         photorealistic mode, disables Midjourney's aesthetic interpretation
--tile        seamlessly tiling/repeating pattern
--draft       10x faster, half GPU cost. V7 only. Good for iteration.
--r 1-40      repeat: generate N image sets (Fast/Turbo mode only)
```

## Image Reference Parameters

```
--sref URL    style reference: captures colors/medium/textures, not content
--sref random random internal style code
--sw 0-1000   style weight (default 100)
--iw 0-3      image weight (default 1). How strongly image prompt influences output.
--oref URL    omni reference (V7): maintain character/object identity. --ow 1-1000
--cref URL    character reference (V6 only). --cw 0-100 (0=face, 100=full)
--p / --p ID  apply personalization profile
```

## Advanced Syntax

### Multi-prompts (weighted concepts)
```
space::2 ship::1    → "space" weighted 2x more than "ship"
```
No space before `::`, one space after.

### Permutations (batch variants)
```
a {red, green, yellow} bird   → 3 separate prompts
--ar {1:1, 16:9, 9:16}        → same prompt in 3 ratios
```

## Best Practices

- Text prompt = content description; `--sref` handles style
- `--raw` + detailed prompt → most photorealistic results
- `--s` low + specific prompt = literal output
- `--s` high = artistic interpretation, less prompt adherence
- `--c > 0` when exploring; `--c 0` when refining
- `--no` accepts specific items only: `--no cake, balloons` (not `--no modern furniture`)
- Combine `--sref` + `--oref` for character + controlled style
- Crop reference images to target aspect ratio before using as image prompts

## Common Aspect Ratios

| Ratio | Use case |
|-------|---------|
| 1:1   | Square, social media |
| 16:9  | Widescreen, video/desktop |
| 9:16  | Vertical, mobile/stories |
| 4:3   | Classic monitor/print |
| 2:3   | Portrait, photo print |

## Example Prompts

```
# Photorealistic portrait
dramatic portrait of elderly fisherman, weathered face, stormy ocean background, soft overcast lighting, desaturated teal palette --ar 2:3 --raw --s 50

# Stylized illustration
cozy witch cottage in enchanted forest, watercolor illustration, warm amber lantern light, muted earthy palette, whimsical mood --ar 4:3 --s 400

# Pattern / texture
seamless botanical pattern, pressed flowers and leaves, cyanotype style, indigo blue on cream --tile --ar 1:1

# Character consistency (V7)
brave knight in silver armor standing at castle gate, dynamic pose, dramatic lighting --oref https://example.com/character.jpg --ow 150 --ar 2:3

# Batch exploration
{photorealistic, watercolor, pixel art} cityscape at night, neon reflections, rain --ar 16:9
```
