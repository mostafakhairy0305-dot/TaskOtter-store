# Spectral Taskfile (npm + nvm)

## What is this Taskfile?

This Taskfile wraps [Spectral](https://stoplight.io/open-source/spectral), a
JSON/YAML linter for OpenAPI, AsyncAPI, and Arazzo documents, with automation
tasks for installing the tool and linting API descriptions. This variant
manages `@stoplight/spectral-cli` as a local devDependency with **npm**, using
**nvm** to provision Node.js — sibling modules cover pnpm and fnm
(`spectral-npm-fnm`, `spectral-pnpm-fnm`, `spectral-pnpm-nvm`). All tasks work
on macOS, Linux, and Windows through the npm-nvm module's platform handling.

## Usage

### Standalone

```bash
task --taskfile taskfiles/spectral-npm-nvm/Taskfile.yml lint TARGETS=openapi.yaml
```

### Included

```yaml
includes:
  spectral:
    taskfile: taskfiles/spectral-npm-nvm/Taskfile.yml
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

## Notes

- Requires the npm-nvm stack: run `task npm:node:setup` first on a fresh
  machine to provision Node.js via nvm.
- `lint` needs `TARGETS` — Spectral prints its usage message when no document
  is given. Without `RULESET`, Spectral discovers `.spectral.yaml` in the
  project automatically; `config:init` scaffolds one extending `spectral:oas`.
- `lint` auto-installs Spectral on first use, and the install `status:` guard
  keeps repeat runs idempotent — changing `VERSION` triggers a reinstall.
