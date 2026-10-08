# Installing Operon in GitHub Copilot CLI

Operon is a token-saving skill that renders bulky files as dense images the agent reads
instead of raw text. It needs no MCP server, no proxy — just Node and this skill.

---

## From a ZIP file (simplest)

Skills are just folders. The `skills/operon/` folder is **self-contained** (bundles
`render.mjs` + the renderer), so installing is a one-liner.

### Easiest — let Copilot register it (recommended)
```bash
unzip operon.zip -d operon                 # or Expand-Archive on Windows
copilot skill add ./operon/skills/operon
copilot skill list                   # confirm "operon" appears
```
`copilot skill add <dir>` registers the directory in your settings — no manual copying,
works from wherever you extracted it.

### Or copy it into the personal skills dir by hand

Personal skills live in `~/.copilot/skills/`:

Windows (PowerShell):
```powershell
Expand-Archive operon.zip -DestinationPath $env:TEMP\operon
New-Item -ItemType Directory -Force "$env:USERPROFILE\.copilot\skills" | Out-Null
Copy-Item $env:TEMP\operon\skills\operon "$env:USERPROFILE\.copilot\skills\operon" -Recurse
```
macOS / Linux:
```bash
unzip operon.zip -d /tmp/operon
mkdir -p ~/.copilot/skills
cp -r /tmp/operon/skills/operon ~/.copilot/skills/operon
```

Verify with `copilot skill list` (shows `operon`), then start a new session.

---

## From this repo (git clone)

```bash
git clone <this-repo-url> operon
copilot skill add ./operon/skills/operon
copilot skill list                   # confirm "operon" appears
```

---

## Use it

In any session, just ask — the skill triggers on the word "operon" or "token-saving mode":

```
using operon, analyze why the request builder in src/providers/*.ts drops image blocks
```
```
operon mode: read these logs and find the first error
```

The agent renders the files to dense PNGs (in a local `.operon-cache/` folder) and reads
those images to answer — cutting input tokens ~45–80%.

> **Best on `gemini-3.1-pro-preview`** (clean ~66% token cut, near-parity accuracy).
> Not recommended on the strongest reasoning models that over-verify dense pages and lose
> the savings.

---

## Repo layout (for maintainers)

```
operon/
├── .claude-plugin/plugin.json     # manifest
├── skills/operon/SKILL.md            # the skill (auto-discovered)
├── skills/operon/render.mjs          # the renderer (run by the skill)
├── skills/operon/vendor/             # pure-JS glyph renderer (no native deps)
├── README.md  EXPERIMENT.md  INSTALL.md
```

The `skills/operon/` folder is self-contained, so distributing just that folder (or a zip of
the repo) is enough.

---

## Uninstall

```bash
copilot skill remove operon
```

## Requirements
- Node 18+ (bundled with most CLI runtimes).
- A vision-capable model, ideally `gemini-3.1-pro-preview`.

## Troubleshooting
- **"render.mjs not found"** — the skill resolves `render.mjs` in its own directory; if the
  agent can't find it, point it at the installed path from `copilot skill list`.
- **Savings look small on a file** — files under 6000 chars are skipped by design (too
  small to beat the image-token floor); they're read as normal text.
- **Exact IDs/strings look wrong** — imaging is lossy; for byte-exact values the agent
  falls back to a normal text Read of that one file. This is expected behavior.
