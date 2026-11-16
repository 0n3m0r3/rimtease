---
title: RimTease Body
description: Anatomy and medical choices, separate from appearance.
---

<p class="rt-eyebrow">Mod catalogue / Anatomy</p>

# RimTease Body

<p class="rt-page-lead">Anatomy with a place in the game.<br>Appearance with a role of its own.</p>

<div class="rt-status"><strong>In development</strong><span>Planned behaviour · RimWorld 1.7 target · No release announced</span></div>

Imagine a character receives a replacement part. The game needs to know which part changed, what it can do, and which medical operation affected it. A visual theme then shows that result. Choosing another theme should leave the character's anatomy and functions intact.

That separation is the purpose of Body.

## What Body is being built to do

<div class="rt-feature-grid">
<section><span class="rt-detail-number">01 / Anatomy</span><h3>Keep individual parts distinct</h3><p>Describe the parts actually present, their side, supported categories and the source of each change. Missing information is not the same as a missing organ.</p></section>
<section><span class="rt-detail-number">02 / Medicine</span><h3>Use the existing medical systems</h3><p>Connect cosmetic changes, grafts and functional replacements to native surgery. Changing appearance does not automatically restore a biological function.</p></section>
<section><span class="rt-detail-number">03 / Equipment</span><h3>Separate coverage from appearance</h3><p>Keep worn, covered, protected and visible distinct. Ordinary clothing should remain usable; a perfect visual fit still needs its own checks.</p></section>
<section><span class="rt-detail-number">04 / Continuity</span><h3>Respect the character's existing state</h3><p>Preserve explicit individual choices and native medical states. Installation, save conversion and removal procedures require verified implementations.</p></section>
</div>

## Anatomy, gameplay and appearance

| Responsibility | Owner |
| --- | --- |
| Anatomical state, medical targets and conditions for native functions | Body |
| Preferences, reactions and activity rules | RimTease core |
| The visual representation of the body and clothes | Themes |
| Reusable technical contracts | RimWeave Framework |

A size category does not add a health, damage or attraction bonus by default. Native systems still own their calculations. Rendering can be optional without making the underlying anatomy optional.

These responsibilities describe the design. They are not an installation dependency list.

## Medical diagrams

The planned Health Display integration would add supported Body parts to the existing medical diagram, preserving native parts. It needs correct textures, positions and side/layer mappings. Compatibility has not yet been verified in game.

[Explore the Health Display visual brief](../docs/visuals/health-display.md)

## Help with Body's visuals

Medical diagram additions, item representations, clear settings and an attachment test marker have different purposes. Some may reuse existing resources; others need decisions before artwork can begin.

[Browse visual requirements by category](../docs/visuals/body.md)

## Availability and installation

No Body package, versioned release or supported load order is announced in this preview. Dependencies and installation steps will be documented with a verified distribution. A description on this page is not evidence that a feature is playable.

[Back to the mod catalogue](../index.md#the-mods) · [Documentation home](../docs/index.md)
