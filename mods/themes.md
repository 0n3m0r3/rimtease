---
title: RimTease Themes
description: Optional body and clothing presentation, independent of anatomy and gameplay.
---

<p class="rt-eyebrow">Mod catalogue / Appearance</p>

# RimTease Themes

<p class="rt-page-lead">A different look.<br>The same character underneath.</p>

<div class="rt-status"><strong>In development</strong><span>Planned behaviour · RimWorld 1.7 target · No release announced</span></div>

Imagine a character has a replacement part, glasses and several layers of clothing. You choose another visual theme, then turn the anatomical renderer off. The intended result is a different presentation of the same character: their parts, medical state, equipment and protection stay intact.

Themes is being designed to make that separation possible. No RimTease renderer or automatic clothing-adaptation prototype has been verified in game.

## What Themes is being built to do

<div class="rt-feature-grid">
<section><span class="rt-detail-number">01 / Appearance</span><h3>Follow the actual body</h3><p>Represent the external structures actually present, including their side and supported size categories. A theme does not create anatomy or replay a medical change.</p></section>
<section><span class="rt-detail-number">02 / Clothing</span><h3>Reuse ordinary clothing</h3><p>Explore local bust adaptation using existing images. Preserve the head, limbs and accessories; a dedicated variant can replace the automatic result when needed.</p></section>
<section><span class="rt-detail-number">03 / Composition</span><h3>Give visual contributions clear roles</h3><p>Define how body layers, clothing, masks and attachment points fit together. Missing variants need an explicit fallback; competing providers need an explicit choice.</p></section>
<section><span class="rt-detail-number">04 / Choice</span><h3>Keep presentation optional</h3><p>Allow the anatomical renderer to be enabled or disabled during play. Turning it off should retain a usable native or third-party presentation and leave the simulation intact.</p></section>
</div>

## How Themes relates to Body

| Responsibility | Owner |
| --- | --- |
| Anatomical state, medical targets and functional clothing coverage | [Body](body.md) and the native systems it integrates with |
| Body and clothing appearance, visual masks and presentation conventions | Themes |
| Preferences, reactions and activity rules | RimTease core |
| Reusable technical contracts | RimWeave Framework |

A graphical mask changes what is drawn. It does not decide what a garment protects. A visible size category does not grant an attraction or health bonus, and disabling Themes does not remove Body.

These are responsibility boundaries, not a verified package or installation dependency list.

## Ordinary clothes, with explicit limits

The proposed first prototype focuses on a classic human body and local bust changes. It would reuse ordinary clothing images across supported sizes instead of requiring a new texture for every garment and size.

That goal still needs verification with soft and rigid garments, multiple layers, four orientations and the portrait. The head, hands, garment hem and unrelated accessories must retain their own proportions. A supplied variant must not receive the same adaptation twice.

Unusual cuts or custom renderers may need a dedicated variant or a fallback to the original image. An imperfect visual fit must not by itself prevent the character from wearing an item. A few successful outfits would not establish compatibility with every clothing mod.

## What still needs to be decided

The initial style, supported silhouettes and categories, layer and mask conventions, exact fallback behaviour and supported third-party configurations remain open. How visual choices are saved and what happens when a theme is removed also need a verified design.

This page does not announce an animation library, furniture pack or complete interface reskin. Activity presentations need their own scope and assets; changing a presentation must not change an activity's gameplay outcome.

## Help with Themes' visuals

The inventory separates body representation, clothing adaptation and evidence captured from the renderer prototype. Medical diagrams and attachment test markers retain their existing briefs under Body.

[Browse Themes' visual requirements](../docs/visuals/themes.md)

## Availability and installation

No Themes package, versioned release, supported load order or in-game compatibility result is announced in this preview. Installation, switching and removal instructions will follow a verified distribution.

[Back to the mod catalogue](../index.md#the-mods) · [Documentation home](../docs/index.md)
