# Module dependency tree

Auto-generated from [`.deps.yml`](.deps.yml).

Regenerate:

```sh
python3 scripts/gen_deps_tree.py
```

**104 modules** total.

## Standalone

Modules with no `includes:` dependencies.

- [`bash-exec`](taskfiles/bash-exec/README.md)
- [`bencher`](taskfiles/bencher/README.md)
- [`bun`](taskfiles/bun/README.md)
- [`docker`](taskfiles/docker/README.md)
- [`fnm`](taskfiles/fnm/README.md)
- [`internal/skipfiles`](taskfiles/internal/skipfiles/Taskfile.yml)
- [`jq`](taskfiles/jq/README.md)
- [`nvm`](taskfiles/nvm/README.md)
- [`uv`](taskfiles/uv/README.md)

## Forward tree

### Node.js stacks

### Depth 0

- `bun`
- `fnm`
- `nvm`

### Depth 1

- `biome-bun` → `bun`, `internal/skipfiles`
- `bruno-bun` → `bun`
- `corepack-fnm` → `fnm`
- `corepack-nvm` → `nvm`
- `depcheck-bun` → `bun`
- `eslint-bun` → `bun`
- `knip-bun` → `bun`, `internal/skipfiles`
- `prettier-bun` → `bun`
- `stylelint-bun` → `bun`
- `typescript-bun` → `bun`

### Depth 2

- `npm-fnm` → `corepack-fnm`, `fnm`
- `npm-nvm` → `corepack-nvm`, `nvm`
- `pnpm-fnm` → `corepack-fnm`, `fnm`
- `pnpm-nvm` → `corepack-nvm`, `nvm`
- `yarn-fnm` → `corepack-fnm`, `fnm`
- `yarn-nvm` → `corepack-nvm`, `nvm`

### Depth 3

- `biome-npm-fnm` → `internal/skipfiles`, `npm-fnm`
- `biome-npm-nvm` → `internal/skipfiles`, `npm-nvm`
- `biome-pnpm-fnm` → `internal/skipfiles`, `pnpm-fnm`
- `biome-pnpm-nvm` → `internal/skipfiles`, `pnpm-nvm`
- `biome-yarn-fnm` → `internal/skipfiles`, `yarn-fnm`
- `biome-yarn-nvm` → `internal/skipfiles`, `yarn-nvm`
- `bruno-npm-fnm` → `npm-fnm`
- `bruno-npm-nvm` → `npm-nvm`
- `bruno-pnpm-fnm` → `pnpm-fnm`
- `bruno-pnpm-nvm` → `pnpm-nvm`
- `bruno-yarn-fnm` → `yarn-fnm`
- `bruno-yarn-nvm` → `yarn-nvm`
- `depcheck-npm-fnm` → `npm-fnm`
- `depcheck-npm-nvm` → `npm-nvm`
- `depcheck-pnpm-fnm` → `pnpm-fnm`
- `depcheck-pnpm-nvm` → `pnpm-nvm`
- `depcheck-yarn-fnm` → `yarn-fnm`
- `depcheck-yarn-nvm` → `yarn-nvm`
- `eslint-npm-fnm` → `npm-fnm`
- `eslint-npm-nvm` → `npm-nvm`
- `eslint-pnpm-fnm` → `pnpm-fnm`
- `eslint-pnpm-nvm` → `pnpm-nvm`
- `eslint-yarn-fnm` → `yarn-fnm`
- `eslint-yarn-nvm` → `yarn-nvm`
- `knip-npm-fnm` → `internal/skipfiles`, `npm-fnm`
- `knip-npm-nvm` → `internal/skipfiles`, `npm-nvm`
- `knip-pnpm-fnm` → `internal/skipfiles`, `pnpm-fnm`
- `knip-pnpm-nvm` → `internal/skipfiles`, `pnpm-nvm`
- `knip-yarn-fnm` → `internal/skipfiles`, `yarn-fnm`
- `knip-yarn-nvm` → `internal/skipfiles`, `yarn-nvm`
- `prettier-npm-fnm` → `npm-fnm`
- `prettier-npm-nvm` → `npm-nvm`
- `prettier-pnpm-fnm` → `pnpm-fnm`
- `prettier-pnpm-nvm` → `pnpm-nvm`
- `prettier-yarn-fnm` → `yarn-fnm`
- `prettier-yarn-nvm` → `yarn-nvm`
- `stylelint-npm-fnm` → `npm-fnm`
- `stylelint-npm-nvm` → `npm-nvm`
- `stylelint-pnpm-fnm` → `pnpm-fnm`
- `stylelint-pnpm-nvm` → `pnpm-nvm`
- `stylelint-yarn-fnm` → `yarn-fnm`
- `stylelint-yarn-nvm` → `yarn-nvm`
- `typescript-npm-fnm` → `npm-fnm`
- `typescript-npm-nvm` → `npm-nvm`
- `typescript-pnpm-fnm` → `pnpm-fnm`
- `typescript-pnpm-nvm` → `pnpm-nvm`
- `typescript-yarn-fnm` → `yarn-fnm`
- `typescript-yarn-nvm` → `yarn-nvm`

### JS tool stacks

**`npm-fnm` stack** — 8 modules (`biome-npm-fnm`, …)

```
biome-npm-fnm
    ├── internal/skipfiles
    └── npm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-npm-fnm`, `bruno-npm-fnm`, `depcheck-npm-fnm`, `eslint-npm-fnm`, `knip-npm-fnm`, `prettier-npm-fnm`, `stylelint-npm-fnm`, `typescript-npm-fnm`

**`npm-nvm` stack** — 8 modules (`biome-npm-nvm`, …)

```
biome-npm-nvm
    ├── internal/skipfiles
    └── npm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-npm-nvm`, `bruno-npm-nvm`, `depcheck-npm-nvm`, `eslint-npm-nvm`, `knip-npm-nvm`, `prettier-npm-nvm`, `stylelint-npm-nvm`, `typescript-npm-nvm`

**`pnpm-fnm` stack** — 8 modules (`biome-pnpm-fnm`, …)

```
biome-pnpm-fnm
    ├── internal/skipfiles
    └── pnpm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-pnpm-fnm`, `bruno-pnpm-fnm`, `depcheck-pnpm-fnm`, `eslint-pnpm-fnm`, `knip-pnpm-fnm`, `prettier-pnpm-fnm`, `stylelint-pnpm-fnm`, `typescript-pnpm-fnm`

**`pnpm-nvm` stack** — 8 modules (`biome-pnpm-nvm`, …)

```
biome-pnpm-nvm
    ├── internal/skipfiles
    └── pnpm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-pnpm-nvm`, `bruno-pnpm-nvm`, `depcheck-pnpm-nvm`, `eslint-pnpm-nvm`, `knip-pnpm-nvm`, `prettier-pnpm-nvm`, `stylelint-pnpm-nvm`, `typescript-pnpm-nvm`

**`yarn-fnm` stack** — 8 modules (`biome-yarn-fnm`, …)

```
biome-yarn-fnm
    ├── internal/skipfiles
    └── yarn-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-yarn-fnm`, `bruno-yarn-fnm`, `depcheck-yarn-fnm`, `eslint-yarn-fnm`, `knip-yarn-fnm`, `prettier-yarn-fnm`, `stylelint-yarn-fnm`, `typescript-yarn-fnm`

**`yarn-nvm` stack** — 8 modules (`biome-yarn-nvm`, …)

```
biome-yarn-nvm
    ├── internal/skipfiles
    └── yarn-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-yarn-nvm`, `bruno-yarn-nvm`, `depcheck-yarn-nvm`, `eslint-yarn-nvm`, `knip-yarn-nvm`, `prettier-yarn-nvm`, `stylelint-yarn-nvm`, `typescript-yarn-nvm`

**`bun` stack** — 8 modules (`biome-bun`, …)

```
biome-bun
    ├── bun
    └── internal/skipfiles
```

`biome-bun`, `bruno-bun`, `depcheck-bun`, `eslint-bun`, `knip-bun`, `prettier-bun`, `stylelint-bun`, `typescript-bun`

**`bun`**

```
bun
```

**`corepack-fnm`**

```
corepack-fnm
    └── fnm
```

**`corepack-nvm`**

```
corepack-nvm
    └── nvm
```

**`fnm`**

```
fnm
```

**`npm-fnm`**

```
npm-fnm
    ├── corepack-fnm
    │   └── fnm
    └── fnm
```

**`npm-nvm`**

```
npm-nvm
    ├── corepack-nvm
    │   └── nvm
    └── nvm
```

**`nvm`**

```
nvm
```

**`pnpm-fnm`**

```
pnpm-fnm
    ├── corepack-fnm
    │   └── fnm
    └── fnm
```

**`pnpm-nvm`**

```
pnpm-nvm
    ├── corepack-nvm
    │   └── nvm
    └── nvm
```

**`yarn-fnm`**

```
yarn-fnm
    ├── corepack-fnm
    │   └── fnm
    └── fnm
```

**`yarn-nvm`**

```
yarn-nvm
    ├── corepack-nvm
    │   └── nvm
    └── nvm
```

### Other chains

### Depth 1

- `actionlint` → `internal/skipfiles`
- `ansible` → `internal/skipfiles`, `uv`
- `buf` → `internal/skipfiles`
- `cargo` → `internal/skipfiles`
- `djlint` → `uv`
- `gh` → `jq`
- `go` → `internal/skipfiles`
- `hadolint` → `internal/skipfiles`
- `jsonlint` → `internal/skipfiles`, `uv`
- `python` → `uv`
- `rumdl` → `uv`
- `shellcheck` → `internal/skipfiles`
- `sqlfluff` → `internal/skipfiles`, `uv`
- `vault` → `jq`
- `yamllint` → `internal/skipfiles`, `uv`
- `zizmor` → `internal/skipfiles`

### Depth 2

- `adrs` → `cargo`
- `dotenv-linter` → `cargo`, `internal/skipfiles`
- `git` → `gh`
- `proto` → `go`
- `protolint` → `go`, `internal/skipfiles`
- `shfmt` → `go`, `internal/skipfiles`
- `staticcheck` → `go`

### Depth 3

- `htmlhint-npm-fnm` → `npm-fnm`
- `htmlhint-npm-nvm` → `npm-nvm`
- `htmlhint-pnpm-fnm` → `pnpm-fnm`
- `htmlhint-pnpm-nvm` → `pnpm-nvm`
- `spectral-npm-fnm` → `npm-fnm`
- `spectral-npm-nvm` → `npm-nvm`
- `spectral-pnpm-fnm` → `pnpm-fnm`
- `spectral-pnpm-nvm` → `pnpm-nvm`

**`actionlint`**

```
actionlint
    └── internal/skipfiles
```

**`adrs`**

```
adrs
    └── cargo
        └── internal/skipfiles
```

**`ansible`**

```
ansible
    ├── internal/skipfiles
    └── uv
```

**`buf`**

```
buf
    └── internal/skipfiles
```

**`cargo`**

```
cargo
    └── internal/skipfiles
```

**`djlint`**

```
djlint
    └── uv
```

**`dotenv-linter`**

```
dotenv-linter
    ├── cargo
    │   └── internal/skipfiles
    └── internal/skipfiles
```

**`gh`**

```
gh
    └── jq
```

**`git`**

```
git
    └── gh
        └── jq
```

**`go`**

```
go
    └── internal/skipfiles
```

**`hadolint`**

```
hadolint
    └── internal/skipfiles
```

**`htmlhint-npm-fnm`**

```
htmlhint-npm-fnm
    └── npm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

**`htmlhint-npm-nvm`**

```
htmlhint-npm-nvm
    └── npm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

**`htmlhint-pnpm-fnm`**

```
htmlhint-pnpm-fnm
    └── pnpm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

**`htmlhint-pnpm-nvm`**

```
htmlhint-pnpm-nvm
    └── pnpm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

**`jsonlint`**

```
jsonlint
    ├── internal/skipfiles
    └── uv
```

**`proto`**

```
proto
    └── go
        └── internal/skipfiles
```

**`protolint`**

```
protolint
    ├── go
    │   └── internal/skipfiles
    └── internal/skipfiles
```

**`python`**

```
python
    └── uv
```

**`rumdl`**

```
rumdl
    └── uv
```

**`shellcheck`**

```
shellcheck
    └── internal/skipfiles
```

**`shfmt`**

```
shfmt
    ├── go
    │   └── internal/skipfiles
    └── internal/skipfiles
```

**`spectral-npm-fnm`**

```
spectral-npm-fnm
    └── npm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

**`spectral-npm-nvm`**

```
spectral-npm-nvm
    └── npm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

**`spectral-pnpm-fnm`**

```
spectral-pnpm-fnm
    └── pnpm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

**`spectral-pnpm-nvm`**

```
spectral-pnpm-nvm
    └── pnpm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

**`sqlfluff`**

```
sqlfluff
    ├── internal/skipfiles
    └── uv
```

**`staticcheck`**

```
staticcheck
    └── go
        └── internal/skipfiles
```

**`vault`**

```
vault
    └── jq
```

**`yamllint`**

```
yamllint
    ├── internal/skipfiles
    └── uv
```

**`zizmor`**

```
zizmor
    └── internal/skipfiles
```

## Reverse tree

For each module, modules that depend on it (direct dependents only).

- `actionlint` — *(none)*
- `adrs` — *(none)*
- `ansible` — *(none)*
- `bash-exec` — *(none)*
- `bencher` — *(none)*
- `biome-bun` — *(none)*
- `biome-npm-fnm` — *(none)*
- `biome-npm-nvm` — *(none)*
- `biome-pnpm-fnm` — *(none)*
- `biome-pnpm-nvm` — *(none)*
- `biome-yarn-fnm` — *(none)*
- `biome-yarn-nvm` — *(none)*
- `bruno-bun` — *(none)*
- `bruno-npm-fnm` — *(none)*
- `bruno-npm-nvm` — *(none)*
- `bruno-pnpm-fnm` — *(none)*
- `bruno-pnpm-nvm` — *(none)*
- `bruno-yarn-fnm` — *(none)*
- `bruno-yarn-nvm` — *(none)*
- `buf` — *(none)*
- `bun` ← `biome-bun`, `bruno-bun`, `depcheck-bun`, `eslint-bun`, `knip-bun`, `prettier-bun`, `stylelint-bun`, `typescript-bun`
- `cargo` ← `adrs`, `dotenv-linter`
- `corepack-fnm` ← `npm-fnm`, `pnpm-fnm`, `yarn-fnm`
- `corepack-nvm` ← `npm-nvm`, `pnpm-nvm`, `yarn-nvm`
- `depcheck-bun` — *(none)*
- `depcheck-npm-fnm` — *(none)*
- `depcheck-npm-nvm` — *(none)*
- `depcheck-pnpm-fnm` — *(none)*
- `depcheck-pnpm-nvm` — *(none)*
- `depcheck-yarn-fnm` — *(none)*
- `depcheck-yarn-nvm` — *(none)*
- `djlint` — *(none)*
- `docker` — *(none)*
- `dotenv-linter` — *(none)*
- `eslint-bun` — *(none)*
- `eslint-npm-fnm` — *(none)*
- `eslint-npm-nvm` — *(none)*
- `eslint-pnpm-fnm` — *(none)*
- `eslint-pnpm-nvm` — *(none)*
- `eslint-yarn-fnm` — *(none)*
- `eslint-yarn-nvm` — *(none)*
- `fnm` ← `corepack-fnm`, `npm-fnm`, `pnpm-fnm`, `yarn-fnm`
- `gh` ← `git`
- `git` — *(none)*
- `go` ← `proto`, `protolint`, `shfmt`, `staticcheck`
- `hadolint` — *(none)*
- `htmlhint-npm-fnm` — *(none)*
- `htmlhint-npm-nvm` — *(none)*
- `htmlhint-pnpm-fnm` — *(none)*
- `htmlhint-pnpm-nvm` — *(none)*
- `internal/skipfiles` ← `actionlint`, `ansible`, `biome-bun`, `biome-npm-fnm`, `biome-npm-nvm`, `biome-pnpm-fnm`, `biome-pnpm-nvm`, `biome-yarn-fnm`, `biome-yarn-nvm`, `buf`, `cargo`, `dotenv-linter`, `go`, `hadolint`, `jsonlint`, `knip-bun`, `knip-npm-fnm`, `knip-npm-nvm`, `knip-pnpm-fnm`, `knip-pnpm-nvm`, `knip-yarn-fnm`, `knip-yarn-nvm`, `protolint`, `shellcheck`, `shfmt`, `sqlfluff`, `yamllint`, `zizmor`
- `jq` ← `gh`, `vault`
- `jsonlint` — *(none)*
- `knip-bun` — *(none)*
- `knip-npm-fnm` — *(none)*
- `knip-npm-nvm` — *(none)*
- `knip-pnpm-fnm` — *(none)*
- `knip-pnpm-nvm` — *(none)*
- `knip-yarn-fnm` — *(none)*
- `knip-yarn-nvm` — *(none)*
- `npm-fnm` ← `biome-npm-fnm`, `bruno-npm-fnm`, `depcheck-npm-fnm`, `eslint-npm-fnm`, `htmlhint-npm-fnm`, `knip-npm-fnm`, `prettier-npm-fnm`, `spectral-npm-fnm`, `stylelint-npm-fnm`, `typescript-npm-fnm`
- `npm-nvm` ← `biome-npm-nvm`, `bruno-npm-nvm`, `depcheck-npm-nvm`, `eslint-npm-nvm`, `htmlhint-npm-nvm`, `knip-npm-nvm`, `prettier-npm-nvm`, `spectral-npm-nvm`, `stylelint-npm-nvm`, `typescript-npm-nvm`
- `nvm` ← `corepack-nvm`, `npm-nvm`, `pnpm-nvm`, `yarn-nvm`
- `pnpm-fnm` ← `biome-pnpm-fnm`, `bruno-pnpm-fnm`, `depcheck-pnpm-fnm`, `eslint-pnpm-fnm`, `htmlhint-pnpm-fnm`, `knip-pnpm-fnm`, `prettier-pnpm-fnm`, `spectral-pnpm-fnm`, `stylelint-pnpm-fnm`, `typescript-pnpm-fnm`
- `pnpm-nvm` ← `biome-pnpm-nvm`, `bruno-pnpm-nvm`, `depcheck-pnpm-nvm`, `eslint-pnpm-nvm`, `htmlhint-pnpm-nvm`, `knip-pnpm-nvm`, `prettier-pnpm-nvm`, `spectral-pnpm-nvm`, `stylelint-pnpm-nvm`, `typescript-pnpm-nvm`
- `prettier-bun` — *(none)*
- `prettier-npm-fnm` — *(none)*
- `prettier-npm-nvm` — *(none)*
- `prettier-pnpm-fnm` — *(none)*
- `prettier-pnpm-nvm` — *(none)*
- `prettier-yarn-fnm` — *(none)*
- `prettier-yarn-nvm` — *(none)*
- `proto` — *(none)*
- `protolint` — *(none)*
- `python` — *(none)*
- `rumdl` — *(none)*
- `shellcheck` — *(none)*
- `shfmt` — *(none)*
- `spectral-npm-fnm` — *(none)*
- `spectral-npm-nvm` — *(none)*
- `spectral-pnpm-fnm` — *(none)*
- `spectral-pnpm-nvm` — *(none)*
- `sqlfluff` — *(none)*
- `staticcheck` — *(none)*
- `stylelint-bun` — *(none)*
- `stylelint-npm-fnm` — *(none)*
- `stylelint-npm-nvm` — *(none)*
- `stylelint-pnpm-fnm` — *(none)*
- `stylelint-pnpm-nvm` — *(none)*
- `stylelint-yarn-fnm` — *(none)*
- `stylelint-yarn-nvm` — *(none)*
- `typescript-bun` — *(none)*
- `typescript-npm-fnm` — *(none)*
- `typescript-npm-nvm` — *(none)*
- `typescript-pnpm-fnm` — *(none)*
- `typescript-pnpm-nvm` — *(none)*
- `typescript-yarn-fnm` — *(none)*
- `typescript-yarn-nvm` — *(none)*
- `uv` ← `ansible`, `djlint`, `jsonlint`, `python`, `rumdl`, `sqlfluff`, `yamllint`
- `vault` — *(none)*
- `yamllint` — *(none)*
- `yarn-fnm` ← `biome-yarn-fnm`, `bruno-yarn-fnm`, `depcheck-yarn-fnm`, `eslint-yarn-fnm`, `knip-yarn-fnm`, `prettier-yarn-fnm`, `stylelint-yarn-fnm`, `typescript-yarn-fnm`
- `yarn-nvm` ← `biome-yarn-nvm`, `bruno-yarn-nvm`, `depcheck-yarn-nvm`, `eslint-yarn-nvm`, `knip-yarn-nvm`, `prettier-yarn-nvm`, `stylelint-yarn-nvm`, `typescript-yarn-nvm`
- `zizmor` — *(none)*
