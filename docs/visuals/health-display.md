---
title: Health Display visual brief
description: Planned medical diagram additions for RimTease Body.
---

<p class="rt-eyebrow">Body / Medicine & integrations</p>

# A medical diagram that follows the body.

<p class="rt-page-lead">Health Display integration</p>

Imagine a Body operation replaces one side of a paired part. Opening the medical diagram should show the part that is actually present, in the correct place, while keeping native parts visible.

<div class="rt-status"><strong>Planned integration</strong><span>Textures and mappings needed · In-game compatibility unverified</span></div>

## The visual requirement

Extend the existing Health Display diagram with the supported Body medical parts. The integration needs textures, positions and mappings to the visualizer's layers. It does not replace RimWorld's health system.

| Situation | The diagram must communicate |
| --- | --- |
| A supported part is present | Its actual occurrence, correct side and intended layer |
| A part was absent from the start | Absence, without implying an amputation |
| A part was removed or replaced | The resulting medical state after the operation and reload |
| A purely cosmetic change | Appearance information, without a disease indicator |
| A texture is missing | Medical information that remains readable |

## What already exists

Health Display provides a medical diagram system, native artwork and texture conventions. Reuse those mechanisms and keep the existing atlas where it is suitable.

The integration is conditional on Health Display being installed. Whether it ships inside Body or in an optional visualizer adapter pack is still undecided. Body's medical data should remain consistent with or without that presentation.

## Decisions before production

- Agree the medical part list and the profiles supported in the first integration.
- Decide which states actually need distinct artwork rather than another display treatment.
- Confirm texture naming, side/layer mappings, positions, dimensions and file formats against the selected visualizer version.
- Establish the provenance and reuse permission for every selected resource.
- Choose the adapter packaging and the comparison scenarios.

No sprite count or universal texture size is prescribed by this brief. Availability of an example file does not grant permission to redistribute it.

## What verification needs to show

The planned checks include paired sides, initially absent parts, grafts, prostheses, save/load, the selected VRE Sanguophage configuration, missing textures, and loading with and without Health Display.

Opening and closing the diagram must not change health, thoughts, simulation randomness or biological functions. Cosmetic presentation must not create false medical capacities to force a drawing into a layer.

These are acceptance goals. None is reported as an executed in-game check here.

## Related work

[Body visual requirements](body.md#medicine-and-integrations) lists the shared inventory. [The Body overview](../../mods/body.md) explains the boundary between anatomy and appearance.
