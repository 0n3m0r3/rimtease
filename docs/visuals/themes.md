---
title: Themes artist brief
description: The body layers, clothing work and comparison captures needed for a RimTease theme.
---

<p class="rt-eyebrow">For creators / Themes</p>

# Make a theme

<p class="rt-page-lead">The body, the clothes, and the checks that bring them together.</p>

<div class="rt-status"><strong>Planning brief</strong><span>The renderer is not ready. File formats, sizes and final asset counts are still undecided.</span></div>

<div class="rt-category-links"><a href="#bodies-and-anatomical-variants">Body layers</a><a href="#clothing-and-masks">Clothing</a><a href="#validation-captures">Comparison captures</a></div>

<h2 id="bodies-and-anatomical-variants">Body layers</h2>

<div class="rt-asset-row">
<figure><img src="../../images/theme-body.svg" width="420" height="240" alt="A body outline keeps its head while its torso changes width."><figcaption>Diagram: change the supported region.</figcaption></figure>
<div><p>Show the external parts the character actually has, on the correct side and at the supported size. Reuse existing head and accessory layers where possible.</p><p><strong>Decide first:</strong> art style, initial body profiles, size categories and the states that need their own drawing.</p></div>
</div>

<details>
<summary>Body mapping and fallback rules</summary>
<ul>
<li>Body owns anatomy. Themes draws it; changing the theme must not create a part or repeat an operation.</li>
<li>Regions, attachment points, masks and drawn versus generated variants still need agreement.</li>
<li>Missing artwork needs a usable fallback. Competing providers need an explicit selection.</li>
<li>Internal organs belong in the medical diagram, not automatically on the map.</li>
</ul>
</details>

## Clothing and masks

<div class="rt-asset-row">
<figure><img src="../../images/theme-clothing.svg" width="420" height="240" alt="Body and clothing layers combine into one dressed character."><figcaption>Diagram: body and clothes stay aligned.</figcaption></figure>
<div><h3>Adapt existing outfits</h3><p>The first prototype should reshape the bust locally using existing clothing images. A dedicated variant can replace that result when needed.</p><p><strong>Prototype first:</strong> choose a small wardrobe and establish what needs an override before drawing a variant for every size.</p></div>
</div>

<details>
<summary>Clothing cases to cover</summary>
<ul>
<li>Check soft and rigid garments, multiple layers, ordinary third-party clothes, unusual openings and custom renderers.</li>
<li>Keep the head, limbs, hem and unrelated accessories unchanged. Never apply the adaptation twice to a supplied variant.</li>
<li>Define masks, override selection and the fallback to the original image. An imperfect fit must not prevent wearing the item.</li>
<li>Body and native systems own coverage and protection. A graphical mask changes only what is drawn.</li>
</ul>
</details>

## Validation captures

<div class="rt-asset-row">
<figure><img src="../../images/theme-checks.svg" width="420" height="240" alt="A comparison sheet shows four directions and a portrait, with rendering off and on."><figcaption>Capture plan: four directions + portrait.</figcaption></figure>
<div><h3>Show the same pawn before and after</h3><p>Capture rendering off and on, every supported size, all four directions and the portrait. Include native and third-party outfits, an override and a fallback.</p><p><strong>Record:</strong> game and mod versions, tested outfits and visible defects. These captures require a working prototype.</p></div>
</div>

<details>
<summary>What the comparison must establish</summary>
<ul>
<li>Inspect contours, stretching, clothing alignment and accessories in the same scene.</li>
<li>Include soft and rigid garments and multiple layers. Successful outfits establish only their own tested coverage.</li>
<li>Measure graphics cost separately. Screenshots cannot prove performance or unchanged simulation.</li>
<li>Check save/load, switching themes, disabling rendering and removing a theme separately.</li>
<li>Keep concept illustrations, finished assets and game captures clearly labelled.</li>
</ul>
</details>

## Shared resources

Use the existing briefs for [medical diagrams](health-display.md), [attachment markers](body.md#attachments-and-test-aids) and [guide illustrations](index.md#shared-documentation-resources). Reuse a suitable comparison capture in a guide.

The mod or pack providing an activity owns its animations and specialist props. This brief does not commission an animation library.

Before using an asset, record its source, author and reuse permission.

[About Themes](../../mods/themes.md) · [All visual briefs](index.md)
