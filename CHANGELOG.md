# Changelog

All notable changes to this workshop will be documented here.

## [Unreleased]

### Changed

- Reframed the public repository as **pre-event only** until 25 May 2026.
- Moved the original 45-minute walkthrough from `workshop/` to `pre-event/playground/` as optional practice material.
- Replaced `workshop/` with an embargo placeholder and publishing checklist for the real event materials.
- Refreshed install docs and version checks against `ai-engineering` `0.8.1` / current `main`.
- Added a central official tooling links page with README/install guide references for base tools, supported IDEs, and optional helpers.
- Clarified that attendees should run `ai-eng install` inside whatever folder/project they want to use for practice, then open their AI agent in that same folder.
- Removed stale `Gemini CLI` and `state.db` references from the active pre-event guide to match current upstream surfaces and files-only persistence.

### Added

- Private, gitignored staging area under `workshop/_private/` for real-project workshop planning and the **La Batalla de las IAs** final challenge.
- Generic pre-event playground flow that does not depend on bundled exercise files.

## [1.0.0] - 2026-05-15

### Added

- Pre-event setup guides (ai-engineering, Engram, RTK, Context7, AgentsView).
- 45-minute workshop walkthrough across the canonical chain.

### Notes

- Targets ai-engineering `framework_version: 0.4.0` and Claude Code as the primary IDE. Copilot, Codex, Gemini, OpenCode, and Cursor are all supported by the framework; commands shown here use the universal `/ai-<skill>` slash syntax.
