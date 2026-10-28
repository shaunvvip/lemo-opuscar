---
name: lemo-opuscar
description: Produce code-rendered short films, explainers and animations with Lemo-Opuscar styles, or create reusable custom styles. Use for Lemo-Opuscar requests and styled film production; not ordinary trimming or transcoding.
---

# Lemo-Opuscar for Codex

This skill stays inside a checkout of the library; do not copy it out on its own.

1. Run `sh "<skill directory>/scripts/setup.sh"` to locate the checkout. It prints `LIB=<absolute path>` and does not fetch, reset or install anything.
2. Read `$LIB/codex/COMPATIBILITY.md`, then `$LIB/AGENTS.md`. Follow the compatibility mapping when the upstream guides name Claude-specific tools. For repository maintenance, work on the requested code; do not start film production.
3. For film production, run the wrapper with `deps` (add `voice` or `music` only when needed). It delegates to the existing upstream setup script in this checkout. Report missing system tools; install project packages only within permitted locations.
4. Read `$LIB/DIRECTOR.md`, `$LIB/TECHNIQUE.md` and the chosen `STYLE.md`. Keep the treatment-before-demo rule and requested storyboard approval. Use the original core tools, absolute project paths and `$LIB` in build scripts.
5. Deliver the complete MP4 and the sources, credits and checks required by DIRECTOR.md. Report separately what was rendered, automatically checked, and actually watched/listened to. A still frame does not validate motion or audio.

In this checkout, projects go in `films/<name>/` (git-ignored). When invoked from another project through the installed skill link, put `<name>/` in the user's working directory. User-specified output locations take precedence. Never put a user's film in `styles/`.

Installation and upstream synchronization: `$LIB/codex/README.md`.
