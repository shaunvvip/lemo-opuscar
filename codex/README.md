# Codex support / Codex 适配

This fork adds a small Codex layer to [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar). The Claude plugin, `core/`, `styles/`, shared guides and licensing remain upstream-compatible. This is not a claim that Codex reproduces the author's Claude-tuned films at equal quality.

## Quick start / 开始使用

Requirements: Git, Node 20+, FFmpeg, and Python 3.11+ (or uv), as in TECHNIQUE.md. The smoke test alone uses Python's standard library. Developed/tested on macOS; other platforms have not been validated by this adaptation.

```sh
git clone https://github.com/shaunvvip/lemo-opuscar.git
cd lemo-opuscar
```

Open this checkout in Codex. The repo-local skill is at `.agents/skills/lemo-opuscar/`; invoke `$lemo-opuscar`, or ask Codex to follow AGENTS.md and codex/COMPATIBILITY.md. For example:

> 用 $lemo-opuscar 做一支 20 秒中文瑞士动态排版短片，讲解密码管理器。1080p，带配音、字幕与音乐，交付完整 MP4 和源码。

To use the skill from other projects, optionally link it into your user skill folder:

```sh
sh codex/install-skill.sh
# Or choose a skill root: sh codex/install-skill.sh /absolute/path/to/skills
```

The installer refuses to overwrite an existing skill. Keep this checkout where it is while the link is installed. Start a new Codex chat if the skill is not discovered. Remove only that symlink to uninstall; films and custom styles are retained. This installer does not install the Claude plugin or modify other skills.

## Dependencies and verification / 依赖与验证

```sh
# Locate checkout only: no downloads or updates
sh .agents/skills/lemo-opuscar/scripts/setup.sh
# Install the shared core dependencies/browser into this checkout
sh .agents/skills/lemo-opuscar/scripts/setup.sh deps
# Optional tiers when a film needs them
sh .agents/skills/lemo-opuscar/scripts/setup.sh deps voice music
# Render and mux a synthetic moving fixture, no voice model needed
python3 codex/test-install.py
python3 codex/smoke-test.py
```

The wrapper reuses `plugin/skills/lemo-opuscar/scripts/setup.sh`; no renderer is duplicated. The smoke test checks frame changes, resolution, frame rate, duration and both encoded streams, then deletes its temporary files. It does not prove Chinese TTS, WebGL style quality, every demo, or normal-speed audiovisual playback. Run production checks in TECHNIQUE.md for each actual film.

The Codex wrapper does not auto-update or reset this checkout. Do not use a `lemo.managed=true` library here: those are upstream's disposable, auto-reset caches. Use a normal clone. Chinese Edge TTS needs network access; dependencies and assets may download from npm, PyPI, GitHub and Hugging Face. Respect the current Codex environment's network, filesystem and browser permissions.

## What changes / 适配范围

- `.agents/skills/lemo-opuscar/`: Codex skill, UI metadata and checkout-local setup wrapper.
- `codex/`: tool mappings, optional symlink installer, runtime smoke test and these instructions.
- Root AGENTS.md and both READMEs: small links to this layer.
- `core/`, `styles/`, the Claude plugin and shared production guides: unchanged.

Production projects remain in `films/<name>/` when working in the library, or in the invoking project's directory when using the global link. Keep original style assets and user projects out of adaptation commits. MIT covers the code; third-party assets retain their own licenses.

## Synchronize upstream / 同步上游

Keep upstream's history; merge updates rather than copying directories or resetting the fork:

```sh
git remote add upstream https://github.com/lemomo-ai/lemo-opuscar.git  # once
# Commit or stash your own edits before synchronizing
git fetch upstream
git switch main
git merge upstream/main
# If conflicts occur, resolve the small root-document links and retain codex/ + .agents/
python3 codex/smoke-test.py
git push origin main
```

Before merging, inspect changes to the shared setup script, guide tool names, rendering CLI and film delivery requirements. Update the Codex mapping only when those contracts change. Review and rerun relevant checks before pushing; never force-reset main to upstream or drop the adaptation layer. Development changes can be reviewed on a topic branch and merged into this fork; an upstream PR is a separate, optional action.

## Optional GitHub Actions / 可选自动测试

`codex/ci-workflow.yml` is a ready-to-enable workflow template. Copy it to
`.github/workflows/codex.yml` and push using credentials permitted to edit workflows
(OAuth tokens need the `workflow` scope). It runs the installer tests and the real
render/mux smoke test on Ubuntu. Until enabled and green, only local macOS results
are established; the template has not been validated on a hosted Linux runner.
The template is kept outside `.github/workflows/` so the adaptation can be pushed
with ordinary repository write access.
