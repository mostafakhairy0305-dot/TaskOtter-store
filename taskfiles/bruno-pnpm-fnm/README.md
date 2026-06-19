# Bruno Taskfile (pnpm-fnm) Public Tasks

## What is this Taskfile?

This Taskfile wraps the [Bruno](https://www.usebruno.com/) CLI (`@usebruno/cli`)
for running API collections from the command line. It installs Bruno as a local
dev dependency This variant uses the `pnpm-fnm` stack (`pnpm-fnm`) package manager.


## Setup

```yaml
includes:
  pnpm:
    taskfile: taskfiles/pnpm-fnm/Taskfile.yml
  bruno:
    taskfile: taskfiles/bruno-pnpm-fnm/Taskfile.yml
```

## Public Tasks

| Task      | Variables                                                    | Description                                              |
| --------- | ------------------------------------------------------------ | -------------------------------------------------------- |
| `install` | Optional `VERSION`, `EXTRA_ARGS`, `CLI_ARGS`           | Install `@usebruno/cli` as a local dev dependency. Pass `VERSION=x.y.z` to pin a release. |
| `install:undo` | Optional `EXTRA_ARGS`                             | Remove the locally installed `@usebruno/cli` devDependency. |
| `upgrade` | Optional `EXTRA_ARGS`                                  | Reinstall `@usebruno/cli` at the latest version.          |
| `run`     | Optional `COLLECTION`, `ENV`, `EXTRA_ARGS`, `CLI_ARGS` | Run all requests in the Bruno collection.                |
| `ci`      | Optional `COLLECTION`, `ENV`, `EXTRA_ARGS`, `CLI_ARGS` | Run collection and stop on the first failure (`--bail`). |
| `version` | — | Show the locally resolved `bru` version.                 |
| `help`    | Optional `EXTRA_ARGS`, `CLI_ARGS`                      | Show Bruno CLI help.                                     |

## Variables

`COLLECTION` is the path to the Bruno collection directory. Defaults to `.`
(the current directory). `ENV` activates a named Bruno environment via
`--env <name>`. `EXTRA_ARGS` and arguments after `--` are appended to the
command.

## Examples

```bash
task bruno:install
task bruno:install VERSION=1.34.1
task bruno:run
task bruno:run COLLECTION=./api ENV=staging
```
