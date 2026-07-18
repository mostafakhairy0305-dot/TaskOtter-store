# Depcheck Taskfile (yarn-fnm) Public Tasks

## What is this Taskfile?

This Taskfile wraps Depcheck for unused and missing dependency reports. It runs
against the project root by default and uses the  for local
binary execution.

## Setup

```yaml
includes:
  yarn:
    taskfile: taskfiles/yarn-fnm/Taskfile.yml
  depcheck:
    taskfile: taskfiles/depcheck-yarn-fnm/Taskfile.yml
```

## Public Tasks

| Task           | Variables                                                                             | Description                                   |
| -------------- | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| `install`      | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS`                                    | Install `depcheck` as a local dev dependency. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo` | Optional `EXTRA_ARGS`                                                           | Remove the locally installed `depcheck` devDependency. |
| `upgrade`      | Optional `EXTRA_ARGS`                                                           | Reinstall `depcheck` at the latest version.   |
| `lint`         | Optional `PROJECT_PATH`, `TARGETS`, `EXTRA_ARGS`, `CLI_ARGS`                    | Run Depcheck.                                 |
| `json`         | Optional `PROJECT_PATH`, `TARGETS`, `EXTRA_ARGS`, `CLI_ARGS`                    | Run Depcheck with `--json`.                   |
| `ignores`      | Optional `PROJECT_PATH`, `TARGETS`, `IGNORE_PACKAGES`, `EXTRA_ARGS`, `CLI_ARGS` | Run Depcheck with ignored packages.           |
| `skip-missing` | Optional `PROJECT_PATH`, `TARGETS`, `EXTRA_ARGS`, `CLI_ARGS`                    | Run Depcheck with `--skip-missing=true`.      |
| `ci`           | Optional `PROJECT_PATH`, `TARGETS`, `EXTRA_ARGS`, `CLI_ARGS`                    | Run Depcheck and fail on findings.            |
| `version`      | — | Show the resolved Depcheck version.           |
| `help`         | Optional `EXTRA_ARGS`, `CLI_ARGS`                                               | Show Depcheck CLI help.                       |

## Variables

`.` and can be overridden for monorepo packages. `TARGETS` is accepted as an
alias for the project path when used from aggregate tasks.

`IGNORE_PACKAGES` is a comma-separated list for the `ignores` task. `EXTRA_ARGS`
and arguments after `--` are appended to the command.

- `DEPCHECK_LINT_SKIP_PATTERN` (default empty): forward-slash path glob for files skipped by lint checks and fixes.

Skip patterns support `*` within one path segment, `**` across directories, and `?` for one character. Paths are matched relative to the task working directory; for example, `**/generated/**`.

## Examples

```bash
task depcheck:install
task depcheck:install VERSION=1.4.7
task depcheck:lint
task depcheck:json
task depcheck:lint PROJECT_PATH=packages/app
task depcheck:lint -- --ignores="@types/*,eslint-*"
```
