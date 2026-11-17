# RimTease — Mods & documentation

The English catalogue and player documentation for RimTease. The preview contains a five-mod demonstration catalogue, individual mod pages, the documentation home, visual requirements grouped by mod, shared documentation resources and the Health Display brief.

The site uses [DocFX](https://dotnet.github.io/docfx/) 2.81.0 with a custom theme. It requires no game installation or backend. The game projects and [RimWeave API documentation](https://0n3m0r3.github.io/rimweave-docs/) remain separate.

## Build and preview

Use .NET 10 and Python 3; this preview was built with SDK 10.0.115 and Python 3.12.3.

From the repository root:

```bash
dotnet tool restore
python3 tools/build.py
python3 tools/serve.py
```

Open <http://localhost:8093/rimtease/>. Keep the terminal running and stop the server with Ctrl+C. Rebuild after editing source files, then reload the browser. Pass `--port 8094` to the preview command if the default port is occupied.

## Content and maintenance

- `index.md` owns the catalogue; `mods/` owns the individual mod pages.
- `docs/` owns player guidance and contribution briefs, organized by mod and category.
- `toc.yml` files define navigation; `templates/rimtease/` owns the presentation.
- `tools/` owns the static build, publication checks and local preview.

The searchable catalogue leads with gameplay additions, followed by the shared foundations. Each mod has a real page with its own URL, illustrated features, required mods and an installation preview. Search and filters survive navigation through mod and dependency pages. Previously shared `#mod-core`, `#mod-body` and `#mod-themes` links redirect to the corresponding pages.

Illustrated covers follow the header's inked, cel-shaded frontier style, with subjects tied to each mod: rope, leather cuffs and a crop for BDSM, a Kamasutra for Extended Positions, a mammary and reproductive anatomy atlas for Body, and underwear, fabrics and furniture finishes for Themes. Four original raster illustrations live in `images/cover-*.png`; the RimTease cover reuses `images/colony-evening.png`. Every cover and the catalogue banner share the transparent `images/rimtease-wordmark.png` logo. The cover name remains HTML text so it stays readable at small sizes. Artwork and wordmark are separate reusable assets; gameplay mock-ups belong inside mod pages. The BDSM equipment room and Extended Positions bedroom have separate images in `images/bdsm-gameplay.png` and `images/positions-gameplay.png`, matching the existing top-down colony illustrations. These scenes illustrate the concepts, not implemented game features. All four covers use the banner as their shared reference, preserving bold black outlines, flat cel shading, matte surfaces and a restrained palette. Body and Themes also have matching top-down scenes in `images/body-gameplay.png` and `images/themes-gameplay.png`. Body illustrates extended anatomy through medical diagrams; Themes compares silhouettes, underwear and room palettes. The furniture variants are an illustration idea, not an approved gameplay scope. This visual identity remains a proposal under review, not a published participation standard.

A demo banner identifies illustrative images, example dependencies and unavailable downloads. The existing demo graph is Body → RimWeave; Themes → RimWeave + Body; RimTease → RimWeave + Body, with Themes optional. Two additional concepts illustrate nested dependencies: BDSM → Extended Positions → RimTease + Body. Both concepts show Themes as optional. The BDSM page distinguishes direct requirements from inherited requirements and provides an expandable dependency tree. Installation previews list each required mod once. These are demonstration choices, not released package manifests or verified load orders. Keep player copy short and put contribution briefs under For creators.

When a feature changes, update its catalogue description and relevant guide or visual brief together. Describe planned, available and verified behaviour separately. A feature's release, dependency or compatibility claim needs evidence from that mod's actual version.

The build versions asset directories by content so returning visitors receive updated styles, scripts and images. The search index travels with its worker in the versioned directory, so content-only changes also invalidate cached search data. Run `python3 -m unittest discover -s tools -p "test_*.py"` to check URL stability and invalidation between publications.

The build treats warnings as errors, checks internal links and anchors, requires every listed content page in search, and rejects private references and game binaries from the generated site. The pinned search adapter fails explicitly when an upstream asset changes. Browser review additionally covers navigation, search, keyboard interaction, mobile layout and theme contrast.

## Delivery

`_site/` is generated and ignored. `.local/` contains temporary build or QA evidence and is ignored.

Two GitHub Actions workflows have separate responsibilities:

- **Validate catalogue and documentation** runs the static build and checks on pushes, pull requests and manual requests.
- **Publish reviewed catalogue and documentation** runs only on a manual request from `main`. It rebuilds and checks the selected revision, records its full commit SHA in `revision.txt`, uploads only `_site/`, and deploys that artifact to GitHub Pages.

The publishing workflow uses GitHub's temporary token and OIDC identity. It needs no personal access token or repository secret. Only the deployment job receives `pages: write` and `id-token: write`. Concurrent publications are serialized.

### First publication

1. Review, commit and push the sources to the chosen GitHub repository's `main` branch. Confirm that the validation workflow passes.
2. In **Settings > Pages > Build and deployment**, select **GitHub Actions** as the source. The repository needs a plan and visibility that support Pages. The deployment environment is named `github-pages`; limit its allowed deployment branches to `main`.
3. After the content and destination have been approved for publication, open **Actions > Publish reviewed catalogue and documentation > Run workflow**, select `main`, and run it.
4. Open the URL reported by the deployment. Verify the home page, a direct link to `docs/visuals/health-display.html`, search and mobile navigation. Fetch `revision.txt` under the same site URL and compare it with the workflow's commit.

See GitHub's [publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom workflow requirements](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

The workflow does not create a repository, enable Pages, configure a domain or publish on push. The final URL comes from the chosen repository's Pages settings; no destination URL is hard-coded in the site. Relative links support a repository subdirectory.

### Updates and rollback

For an update, review and publish the source changes, let validation pass, then manually run the publishing workflow from `main`.

To return to previous content, revert the relevant source changes in a new commit on `main`, review the diff, and publish that commit through the same validation and manual deployment process. This preserves history; do not reset or force-push the branch. Verify the live site and `revision.txt` after the deployment. The rollback is a new source revision whose content restores the earlier version.

Deployment and rollback require verification on the configured GitHub repository. A successful local build does not establish that either has run. This preview does not announce a RimTease release or provide installation instructions for an unverified package.

## License

Original documentation and tooling are licensed under [MIT](LICENSE). See [third-party notices](THIRD-PARTY-NOTICES.md) for reused tooling.
