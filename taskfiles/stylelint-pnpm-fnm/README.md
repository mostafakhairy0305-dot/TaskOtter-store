# Stylelint Taskfile (pnpm-fnm) Public Tasks

## What is this Taskfile?

This Taskfile wraps Stylelint for stylesheet checks and fixes. It installs
`stylelint` and `stylelint-config-standard` locally, enables cache by default,

## Setup

```yaml
includes:
  pnpm:
    taskfile: taskfiles/pnpm-fnm/Taskfile.yml
  stylelint:
    taskfile: taskfiles/stylelint-pnpm-fnm/Taskfile.yml
```

## Public Tasks

| Task          | Variables                                                                                  | Description                                                          |
| ------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| `install`     | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS`                                         | Install Stylelint and the standard config as local dev dependencies. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo`| Optional `EXTRA_ARGS`                                                                | Remove the locally installed Stylelint devDependencies.              |
| `upgrade`     | Optional `EXTRA_ARGS`                                                                | Reinstall Stylelint and the standard config at their latest versions. |
| `config:init` | Optional `CONFIG`                                                                          | Create a starter Stylelint config when one does not exist.           |
| `lint`        | Optional `TARGETS`, `CONFIG`, `CACHE`, `ALLOW_EMPTY_INPUT`, `EXTRA_ARGS`, `CLI_ARGS` | Lint stylesheet targets.                                             |
| `lint:fix`    | Optional `TARGETS`, `CONFIG`, `CACHE`, `ALLOW_EMPTY_INPUT`, `EXTRA_ARGS`, `CLI_ARGS` | Run Stylelint with `--fix`.                                          |
| `ci`          | Optional `TARGETS`, `CONFIG`, `CACHE`, `ALLOW_EMPTY_INPUT`, `EXTRA_ARGS`, `CLI_ARGS` | Run Stylelint with `--max-warnings=0`.                               |
| `cache:clean` | —                                                                                          | Remove `.cache/stylelint`.                                           |
| `version`     | — | Show the resolved Stylelint version.                                 |
| `help`        | Optional `EXTRA_ARGS`, `CLI_ARGS`                                                    | Show Stylelint CLI help.                                             |

## Variables

`**/*.{css,scss,sass,less,vue,svelte,astro}`. `CONFIG` adds `--config <path>`.

`CACHE` and `ALLOW_EMPTY_INPUT` both default to `true`; set either to `false`
to omit that flag. `EXTRA_ARGS` and arguments after `--` are appended to the
command.

- `STYLELINT_LINT_SKIP_PATTERN` (default empty): forward-slash path glob for files skipped by lint checks and fixes.

Skip patterns support `*` within one path segment, `**` across directories, and `?` for one character. Paths are matched relative to the task working directory; for example, `**/generated/**`.

## Examples

```bash
task stylelint:install
task stylelint:install VERSION=16.6.1
task stylelint:lint
task stylelint:lint:fix TARGETS="src/**/*.scss"
```
