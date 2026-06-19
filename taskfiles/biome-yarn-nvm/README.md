# Biome Taskfile (yarn-nvm) Public Tasks

## What is this Taskfile?

This Taskfile wraps Biome for formatting, linting, combined checks, and CI. It
installs `@biomejs/biome` locally and delegates package-manager behavior to the

## Setup

```yaml
includes:
  yarn:
    taskfile: taskfiles/yarn-nvm/Taskfile.yml
  biome:
    taskfile: taskfiles/biome-yarn-nvm/Taskfile.yml
```

## Public Tasks

| Task           | Variables                                                    | Description                                                                |
| -------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------- |
| `install`      | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS`           | Install `@biomejs/biome` as a local dev dependency. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo` | Optional `EXTRA_ARGS`                                  | Remove the locally installed `@biomejs/biome` devDependency.               |
| `upgrade`      | Optional `EXTRA_ARGS`                                  | Reinstall `@biomejs/biome` at the latest version.                          |
| `init`         | Optional `EXTRA_ARGS`, `CLI_ARGS`                      | Alias for `config:init`.                                                   |
| `config:init`  | Optional `EXTRA_ARGS`, `CLI_ARGS`                      | Run `biome init`. Skipped if `biome.json` or `biome.jsonc` already exists. |
| `check`        | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome check`.                                                         |
| `check:write`  | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome check --write`.                                                 |
| `fix`          | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Alias for `check:write`.                                                   |
| `lint`         | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome lint`.                                                          |
| `lint:fix`     | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome lint --write`.                                                  |
| `fmt:check`    | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome format`.                                                        |
| `fmt`          | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome format --write`.                                                |
| `ci`           | Optional `TARGETS`, `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `biome ci`.                                                            |
| `cache:clean`  | —                                                            | Remove common Biome cache directories.                                     |
| `version`      | — | Show the resolved Biome version.                                           |
| `help`         | Optional `EXTRA_ARGS`, `CLI_ARGS`                      | Show Biome CLI help.                                                       |

## Variables

and `CONFIG` adds `--config-path <path>`.

`EXTRA_ARGS` and arguments after `--` are appended to the command.

## Examples

```bash
task biome:install
task biome:install VERSION=1.9.4
task biome:config:init
task biome:check
task biome:check:write
task biome:lint
task biome:fmt
```
