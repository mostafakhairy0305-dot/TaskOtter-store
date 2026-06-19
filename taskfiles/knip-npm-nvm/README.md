# Knip Taskfile (npm-nvm) Public Tasks

## What is this Taskfile?

This Taskfile wraps Knip for unused file, export, and dependency analysis. Knip
can report framework-specific false positives, so treat output as review input
instead of an instruction to delete files or packages automatically.

## Setup

```yaml
includes:
  npm:
    taskfile: taskfiles/npm-nvm/Taskfile.yml
  knip:
    taskfile: taskfiles/knip-npm-nvm/Taskfile.yml
```

## Public Tasks

| Task               | Variables                                         | Description                                               |
| ------------------ | ------------------------------------------------- | --------------------------------------------------------- |
| `install`          | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS` | Install `knip` as a local dev dependency. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo`     | Optional `EXTRA_ARGS`                       | Remove the locally installed `knip` devDependency.         |
| `upgrade`          | Optional `EXTRA_ARGS`                       | Reinstall `knip` at the latest version.                    |
| `init`             | Optional `EXTRA_ARGS`, `CLI_ARGS`           | Initialize Knip configuration.                            |
| `config:init`      | Optional `EXTRA_ARGS`, `CLI_ARGS`           | Alias for `init`.                                         |
| `lint`             | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run the default Knip analysis.                            |
| `production`       | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run Knip with `--production`.                             |
| `dependencies`     | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Report unused production dependencies.                    |
| `dev-dependencies` | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Report unused development dependencies.                   |
| `files`            | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Report unused files.                                      |
| `exports`          | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Report unused exports.                                    |
| `lint:fix`         | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run `knip --fix` when supported by the installed version. |
| `ci`               | Optional `CONFIG`, `EXTRA_ARGS`, `CLI_ARGS` | Run production checks for CI.                             |
| `version`          | — | Show the resolved Knip version.                           |
| `help`             | Optional `EXTRA_ARGS`, `CLI_ARGS`           | Show Knip CLI help.                                       |

## Variables

`--config <path>`. `EXTRA_ARGS` and arguments after `--` are appended to the
command.

Review Knip findings before deleting files or dependencies.

## Examples

```bash
task knip:install
task knip:install VERSION=5.27.0
task knip:lint
task knip:production
task knip:dependencies
task knip:files
task knip:exports
```
