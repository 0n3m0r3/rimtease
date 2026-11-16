---
title: Body visual requirements
description: Medical visuals, interfaces and attachment test aids for RimTease Body.
---

<p class="rt-eyebrow">Documentation / Visual requirements / Body</p>

# Body visual requirements

<p class="rt-page-lead">A clear purpose for every visual.</p>

Start with the category you want to help with. Each need belongs to Body unless another owner is named. On-map body appearance and clothing adaptation belong to [Themes](themes.md); they use Body's state.

<div class="rt-status"><strong>Planning inventory</strong><span>Artwork and in-game integration are not verified by this page.</span></div>

<div class="rt-category-links"><a href="#medicine-and-integrations">Medicine & integrations</a><a href="#interfaces-and-settings">Interfaces & settings</a><a href="#attachments-and-test-aids">Attachments & test aids</a><a href="#guide-illustrations">Guide illustrations</a></div>

## Medicine and integrations

### Medical diagram additions

<span class="rt-label">Required representation · Integration pending</span>

Add supported Body parts to Health Display's existing medical diagram on the correct side and layer. Preserve its native atlas. Distinguish a part absent from the start from a part that was removed or replaced.

**Owner:** Body integration with Health Display.\
**Possible reuse:** the visualizer's diagram system and existing native atlas.\
**Decisions still open:** final medical part list, state variants, supported profiles, texture mappings and adapter packaging.

A cosmetic change must not look like a disease. This is a planned integration, not a verified compatibility claim.

[Read the complete Health Display brief](health-display.md)

### Medical item representations

<span class="rt-label">Representation required · Original artwork undecided</span>

Selected cosmetic implants, biological grafts and functional replacements need recognizable inventory and trade representations. Generic medical graphics may suffice.

**Owner:** Body.\
**Possible reuse:** suitable native medical representations and the existing implant workflow.\
**Decisions still open:** the actual item and recipe list, dedicated versus generic artwork, and the source and reuse rights of each file.

A native DLC implant is a design reference, not permission to copy its assets or add a new DLC requirement. Agree the item list before estimating a sprite count.

## Interfaces and settings

### Settings, medical choices and removal reports

<span class="rt-label">Readable interface required · Native controls preferred</span>

Show understandable size categories, generation scope, value provenance, surgical targets and functional reasons. Conversion or removal reports must explain what will be retained or lost.

**Owner:** Body.\
**Possible reuse:** native sliders, medical lists and recipe interfaces.\
**Decisions still open:** exact screens, pilot profiles and conversion choices.

The graphical medical atlas is a separate need. Disabling a renderer must never be described as removing Body.

## Attachments and test aids

### An attachment test marker

<span class="rt-label">Validation aid · First consumer undecided</span>

Use a simple marker to show which exact body occurrence an attachment targets. Check left and right, size changes, a missing support and reloading.

**Owner:** Body, with Themes for presentation.\
**Possible reuse:** a simple test shape or an authorized resource.\
**Decisions still open:** the first target, its support and the first consumer.

Selection may use a contextual list. Tiny clickable regions on the pawn image are not required. This test aid does not commission a specialist-equipment catalogue.

## Guide illustrations

[Explanatory diagrams and annotated screenshots](index.md#shared-documentation-resources) belong to the documentation. Potential Body examples include size settings, surgical choices, the medical atlas and preparation for removal. Keep their shared brief and source in one place.

## Before starting artwork

1. Confirm the feature, the owner and whether an existing resource is sufficient.
2. Agree supported variants and display context. Dimensions, formats, naming and quantities remain open until the target integration is defined.
3. Record the source, author and permission to use each resource.
4. Keep concept previews, final artwork and in-game verification distinct.

[About RimTease Body](../../mods/body.md) · [All visual requirements](index.md)
