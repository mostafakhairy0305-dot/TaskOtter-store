# HTMLHint Taskfile (npm + nvm)

## What is this Taskfile?

This Taskfile wraps [HTMLHint](https://htmlhint.com/), a static analysis tool
for HTML, with automation tasks for installing the tool and linting HTML
files. This variant manages HTMLHint as a local devDependency with **npm**,
using **nvm** to provision Node.js — sibling modules cover pnpm and fnm
(`htmlhint-npm-fnm`, `htmlhint-pnpm-fnm`, `htmlhint-pnpm-nvm`). All tasks work
on macOS, Linux, and Windows through the npm-nvm module's platform handling.

## Usage

### Standalone

```bash
task --taskfile taskfiles/htmlhint-npm-nvm/Taskfile.yml lint TARGETS="src/**/*.html"
```

### Included

```yaml
includes:
  htmlhint:
    taskfile: taskfiles/htmlhint-npm-nvm/Taskfile.yml
```

```bash
task htmlhint:install
task htmlhint:lint TARGETS="src/**/*.html"
task htmlhint:lint CONFIG=.htmlhintrc
task htmlhint:install VERSION=1.7.1
```

Run the tasks from the Node.js project root (where `package.json` lives).

## Public Tasks

| Task | Description | Key variables |
|---|---|---|
| `install` | Install HTMLHint as a local devDependency | `VERSION` |
| `install:undo` | Remove the HTMLHint devDependency (alias: `uninstall`) | |
| `upgrade` | Upgrade HTMLHint to the latest release | |
| `lint` | Lint HTML files with HTMLHint | `TARGETS`, `CONFIG`, `EXTRA_ARGS` |
| `config:init` | Create a default .htmlhintrc configuration file | |
| `help` | Show the HTMLHint CLI help | |
| `version` | Show the locally resolved HTMLHint version | |

## Variables

| Variable | Default | Description |
|---|---|---|
| `VERSION` | `""` (package manager default) | Pin a specific htmlhint release |
| `TARGETS` | `**/*.html` | Glob of HTML files to lint |
| `CONFIG` | `""` | Path to a custom HTMLHint configuration file |
| `EXTRA_ARGS` | `""` | Extra flags forwarded to htmlhint |
| `HTMLHINT_LINT_SKIP_PATTERN` | _(empty)_ | Forward-slash path glob for files skipped by lint checks and fixes |

Skip patterns support `*` within one path segment, `**` across directories, and `?` for one character. Paths are matched relative to the task working directory; for example, `**/generated/**`.

## Notes

- Requires the npm-nvm stack: run `task npm:node:setup` first on a fresh
  machine to provision Node.js via nvm.
- `lint` auto-installs HTMLHint on first use, and the install `status:` guard
  keeps repeat runs idempotent — changing `VERSION` triggers a reinstall.
- HTMLHint is lint-only; it has no autofix mode.
