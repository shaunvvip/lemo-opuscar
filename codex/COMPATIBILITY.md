# Codex mapping for the upstream film guides

Read this together with AGENTS.md, DIRECTOR.md and TECHNIQUE.md. The upstream style rules and production tools remain shared with Claude Code.

- `AskUserQuestion`: use the current Codex question tool when available and appropriate, otherwise ask in plain text. Never call a tool that does not exist. Preserve choices, free conversation, and real approval gates, including storyboard and saving custom styles. Reuse answers already provided by the user; an unanswered required question is not approval.
- `/lemo-opuscar:lemo-opuscar`: invoke `$lemo-opuscar` in Codex, or request the workflow in ordinary language. `claude plugin ...` commands apply only to Claude Code.
- Setup: use `.agents/skills/lemo-opuscar/scripts/setup.sh` from this checkout instead of the shared skill's default download entry. This keeps this fork's Codex additions and the user's chosen revision. It never automatically pulls or resets the checkout. Dependencies and assets still use the upstream scripts.
- Paths: respect the user's writable workspace and sandbox. Missing permission for network, browser execution or another output directory must be resolved through the host permission flow. Do not silently relocate custom styles or claim an installation succeeded when access was denied.
- Long renders: use available command sessions and bounded polls; report meaningful progress. Stop only child processes launched for this task. Keep build commands reproducible in the film's build.sh.
- Review: run the upstream still, readability, ASR, black-frame and audio checks when applicable. Inspect representative frames and key-action strips. If full-speed audiovisual playback is unavailable, say that clearly; do not label the film playback-verified. Provide the final MP4 for the user to play.
- Model: the original style prompts were tuned for Claude; Codex compatibility does not establish visual parity. Preserve style invariants and evaluate a real film rather than claiming equal quality.

For maintenance, installation, synchronization or questions about this repository, do that task directly. The film intake and treatment workflow applies to making films, not to maintenance.
