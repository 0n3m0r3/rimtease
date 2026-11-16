# RimTease — Mods & documentation

The English catalogue and player documentation for RimTease. The preview contains the mod catalogue, Body and Themes overviews, the documentation home, visual requirements grouped by mod, shared documentation resources and the Health Display brief.

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

- `index.md` owns the catalogue; `mods/` owns the detailed Body and Themes descriptions.
- `docs/` owns player guidance and contribution briefs, organized by mod and category.
- `toc.yml` files define navigation; `templates/rimtease/` owns the presentation.
- `tools/` owns the static build, publication checks and local preview.

The home page addresses players and clearly marks RimTease as intended for adults. Use brief descriptions and useful illustrations; keep detailed contributor constraints in expandable sections. Label concept artwork and diagrams so they cannot be mistaken for game captures. The current redesign covers the home page, guide entry and Themes artist brief; the other detailed pages still need editorial review.

When a feature changes, update its catalogue description and relevant guide or visual brief together. Describe planned, available and verified behaviour separately. A feature's release, dependency or compatibility claim needs evidence from that mod's actual version.

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
