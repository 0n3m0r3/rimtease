---
title: Themes visual requirements
description: Body appearance, clothing adaptation and renderer comparison captures for RimTease Themes.
---

<p class="rt-eyebrow">Documentation / Visual requirements / Themes</p>

# Themes visual requirements

<p class="rt-page-lead">Change the presentation.<br>Keep the character's state.</p>

Imagine comparing the same clothed character with the renderer disabled and enabled. These needs describe the body layers, clothing treatment and comparison evidence required for that planned presentation. Themes reads Body's actual state; anatomy, medical rules and protection keep their own owners.

<div class="rt-status"><strong>Planning inventory</strong><span>Art briefs and the renderer prototype remain to be defined. No in-game result is verified here.</span></div>

<div class="rt-category-links"><a href="#bodies-and-anatomical-variants">Bodies & anatomical variants</a><a href="#clothing-and-masks">Clothing & masks</a><a href="#validation-captures">Validation captures</a><a href="#shared-resources">Shared resources</a></div>

## Bodies and anatomical variants

### Body appearance

<span class="rt-label">Required for the planned renderer · Art brief pending</span>

Represent the external structures actually present, their side and supported size categories. A missing or replaced part must follow Body's state. Internal medical organs belong in the medical diagram; their existence does not automatically require an on-map graphic.

**Owner:** Themes, using Body data.\
**Variants to define:** initial silhouettes and profiles, supported size categories, sides, absent or replacement states, and the views the renderer supports.\
**Possible reuse:** valid native or third-party body, head and accessory layers, with their source and reuse rights checked.\
**Decisions still open:** visual style, drawn versus generated variants, regions, anchors, masks, file specifications and the first supported configurations.

An incomplete theme needs a usable fallback. If two providers represent the same element, the selection or resolution must be explicit. No sprite count or universal body-profile support is established by this inventory.

## Clothing and masks

### Clothing adaptation

<span class="rt-label">Existing images preferred · Automatic adaptation unverified</span>

The planned automatic path adapts the relevant upper-body layers locally while preserving the head, limbs and unrelated accessories. It aims to support ordinary clothing across size categories without commissioning one texture per garment and size.

**Owner:** Themes for appearance; Body and native systems retain functional coverage and protection.\
**Cases to cover:** soft and rigid garments, multiple layers, ordinary third-party clothing, unusual openings, dedicated variants and unsupported renderers.\
**Possible reuse:** existing clothing images and a supplied variant when the automatic path is unsuitable. A dedicated variant must not be deformed twice.\
**Decisions still open:** prototype feasibility, pilot wardrobe, supported categories, mask conventions, fallback rules and the conditions for selecting an override.

A mask may hide a layer without changing protection. A garment may remain wearable even when its original image is the only usable fallback. Do not commission replacements for an entire wardrobe before the prototype establishes what can be reused.

## Validation captures

### Renderer comparison captures

<span class="rt-label">Required prototype evidence · Not yet captured</span>

Show whether the planned renderer preserves contours, clothing alignment and unrelated body regions. These are captures of a working prototype, not a request for illustrative artwork.

**Owner:** Themes, with Body review.\
**Required comparisons:** rendering disabled and enabled, supported categories, all four orientations and the portrait in the same versioned scene. Include native and ordinary third-party clothing, multiple layers, soft and rigid garments, a dedicated override and a fallback.\
**Possible reuse:** one suitable comparison capture may also illustrate a player guide; keep a single source and identify the context.\
**Decisions still open:** the representative scene, wardrobe, supported configurations and capture procedure.

Review contours, stretching, layer alignment, accessories and the result of toggling the renderer. Record the game and mod versions and which cases passed or failed. Graphics-cost measurements are separate evidence; still images alone cannot establish performance or prove that simulation state is unchanged.

Successful examples cover only the configurations actually checked. Save/load, theme removal and simulation-preservation checks remain separate obligations.

## Shared resources

| Related need | Existing owner and brief |
| --- | --- |
| Internal parts, sides and medical states in a medical diagram | Body's [Health Display integration](health-display.md) |
| An observable target for an attachment | Body's [attachment test marker](body.md#attachments-and-test-aids), with Themes for presentation |
| Explanations of anatomy, coverage and appearance | [Shared documentation diagrams](index.md#explanatory-diagrams) |
| Rendering settings and theme-comparison illustrations | [Shared guide screenshots](index.md#guide-screenshots); reuse a suitable prototype comparison |

Activity animations and specialist equipment belong with their selected consumer or content provider. This inventory does not create a second animation or accessory catalogue.

## Before starting artwork

Confirm the feature, owner, supported variants and opportunity for reuse first. Dimensions, formats, naming and quantities follow the chosen integration. Record each resource's source, author and usage rights, and keep concept previews, final artwork and in-game verification distinct.

[About RimTease Themes](../../mods/themes.md) · [All visual requirements](index.md)
