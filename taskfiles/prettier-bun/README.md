# Prettier Taskfile (bun) Public Tasks

## What is this Taskfile?

This Taskfile wraps Prettier checks and writes for JavaScript/TypeScript
projects and workspaces. It uses the  for local binary
execution and package-manager detection.

## Setup

```yaml
includes:
  bun:
    taskfile: taskfiles/bun/Taskfile.yml
  prettier:
    taskfile: taskfiles/prettier-bun/Taskfile.yml
```

## Public Tasks

| Task          | Variables                                                                   | Description                                               |
| ------------- | --------------------------------------------------------------------------- | --------------------------------------------------------- |
| `install`     | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS`                          | Install `prettier` as a local dev dependency. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo`| Optional `EXTRA_ARGS`                                                 | Remove the locally installed `prettier` devDependency.    |
| `upgrade`     | Optional `EXTRA_ARGS`                                                 | Reinstall `prettier` at the latest version.                |
| `config:init` | Optional `CONFIG`                                                           | Create a starter Prettier config when one does not exist. |
| `fmt:check`   | Optional `TARGETS`, `CONFIG`, `IGNORE_PATH`, `EXTRA_ARGS`, `CLI_ARGS` | Run `prettier --check`.                                   |
| `fmt`         | Optional `TARGETS`, `CONFIG`, `IGNORE_PATH`, `EXTRA_ARGS`, `CLI_ARGS` | Run `prettier --write`.                                   |
| `fix`         | Optional `TARGETS`, `CONFIG`, `IGNORE_PATH`, `EXTRA_ARGS`, `CLI_ARGS` | Alias for `fmt`.                                           |
| `ci`          | Optional `TARGETS`, `CONFIG`, `IGNORE_PATH`, `EXTRA_ARGS`, `CLI_ARGS` | Alias for `fmt:check`.                                     |
| `version`     | — | Show the resolved Prettier version.                       |
| `help`        | Optional `EXTRA_ARGS`, `CLI_ARGS`                                     | Show Prettier CLI help.                                   |

## Variables

`CONFIG` adds `--config <path>`, and `IGNORE_PATH` defaults to
`.prettierignore`. The ignore path is only passed when the file exists.

`EXTRA_ARGS` and arguments after `--` are appended to the command.

- `PRETTIER_FMT_SKIP_PATTERN` (default empty): forward-slash path glob for files skipped by formatting checks and fixes.

Skip patterns support `*` within one path segment, `**` across directories, and `?` for one character. Paths are matched relative to the task working directory; for example, `**/generated/**`.

## Examples

```bash
task prettier:install
task prettier:install VERSION=3.3.3
task prettier:fmt:check
task prettier:fmt TARGETS="src/**/*.ts"
```
