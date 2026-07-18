# Spectral Taskfile (pnpm + fnm)

## What is this Taskfile?

This Taskfile wraps [Spectral](https://stoplight.io/open-source/spectral), a
JSON/YAML linter for OpenAPI, AsyncAPI, and Arazzo documents, with automation
tasks for installing the tool and linting API descriptions. This variant
manages `@stoplight/spectral-cli` as a local devDependency with **pnpm**,
using **fnm** to provision Node.js — sibling modules cover npm and nvm
(`spectral-npm-fnm`, `spectral-npm-nvm`, `spectral-pnpm-nvm`). All tasks work
on macOS, Linux, and Windows through the pnpm-fnm module's platform handling.

## Usage

### Standalone

```bash
task --taskfile taskfiles/spectral-pnpm-fnm/Taskfile.yml lint TARGETS=openapi.yaml
```

### Included

```yaml
includes:
  spectral:
    taskfile: taskfiles/spectral-pnpm-fnm/Taskfile.yml
```

```bash
task spectral:install
task spectral:config:init
task spectral:lint TARGETS=openapi.yaml
task spectral:lint TARGETS=openapi.yaml RULESET=.spectral.yaml
task spectral:install VERSION=6.15.0
```

Run the tasks from the Node.js project root (where `package.json` lives).

## Public Tasks

| Task | Description | Key variables |
|---|---|---|
| `install` | Install Spectral as a local devDependency | `VERSION` |
| `install:undo` | Remove the Spectral devDependency (alias: `uninstall`) | |
| `upgrade` | Upgrade Spectral to the latest release | |
| `lint` | Lint API documents with Spectral | `TARGETS`, `RULESET`, `EXTRA_ARGS` |
| `config:init` | Create a default .spectral.yaml ruleset | |
| `help` | Show the Spectral CLI help | |
| `version` | Show the locally resolved Spectral version | |

## Variables

| Variable | Default | Description |
|---|---|---|
| `VERSION` | `""` (package manager default) | Pin a specific @stoplight/spectral-cli release |
| `TARGETS` | `""` | API document(s) to lint, e.g. `openapi.yaml` |
| `RULESET` | `""` | Path to a Spectral ruleset file passed via `--ruleset` |
| `EXTRA_ARGS` | `""` | Extra flags forwarded to spectral |
| `SPECTRAL_LINT_SKIP_PATTERN` | _(empty)_ | Forward-slash path glob for files skipped by lint checks and fixes |

Skip patterns support `*` within one path segment, `**` across directories, and `?` for one character. Paths are matched relative to the task working directory; for example, `**/generated/**`.

Spectral skips matching files as top-level lint targets, but may still load them when another document references them through `$ref`.

## Notes

- Requires the pnpm-fnm stack: run `task pnpm:node:setup` first on a fresh
  machine to provision Node.js via fnm.
- `lint` needs `TARGETS` — Spectral prints its usage message when no document
  is given. Without `RULESET`, Spectral discovers `.spectral.yaml` in the
  project automatically; `config:init` scaffolds one extending `spectral:oas`.
- `lint` auto-installs Spectral on first use, and the install `status:` guard
  keeps repeat runs idempotent — changing `VERSION` triggers a reinstall.
