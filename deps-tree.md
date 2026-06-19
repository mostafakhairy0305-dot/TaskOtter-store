# Module dependency tree

Auto-generated from [`.deps.yml`](.deps.yml).

Regenerate:

```sh
python3 scripts/gen_deps_tree.py
```

**85 modules** total.

## Standalone

Modules with no `includes:` dependencies.

- [`actionlint`](taskfiles/actionlint/README.md)
- [`buf`](taskfiles/buf/README.md)
- [`bun`](taskfiles/bun/README.md)
- [`docker`](taskfiles/docker/README.md)
- [`fnm`](taskfiles/fnm/README.md)
- [`go`](taskfiles/go/README.md)
- [`hadolint`](taskfiles/hadolint/README.md)
- [`jq`](taskfiles/jq/README.md)
- [`nvm`](taskfiles/nvm/README.md)
- [`shellcheck`](taskfiles/shellcheck/README.md)
- [`uv`](taskfiles/uv/README.md)
- [`zizmor`](taskfiles/zizmor/README.md)

## Forward tree

### Node.js stacks

### Depth 0

- `bun`
- `fnm`
- `nvm`

### Depth 1

- `biome-bun` → `bun`
- `bruno-bun` → `bun`
- `corepack-fnm` → `fnm`
- `corepack-nvm` → `nvm`
- `depcheck-bun` → `bun`
- `eslint-bun` → `bun`
- `knip-bun` → `bun`
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

- `biome-npm-fnm` → `npm-fnm`
- `biome-npm-nvm` → `npm-nvm`
- `biome-pnpm-fnm` → `pnpm-fnm`
- `biome-pnpm-nvm` → `pnpm-nvm`
- `biome-yarn-fnm` → `yarn-fnm`
- `biome-yarn-nvm` → `yarn-nvm`
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
- `knip-npm-fnm` → `npm-fnm`
- `knip-npm-nvm` → `npm-nvm`
- `knip-pnpm-fnm` → `pnpm-fnm`
- `knip-pnpm-nvm` → `pnpm-nvm`
- `knip-yarn-fnm` → `yarn-fnm`
- `knip-yarn-nvm` → `yarn-nvm`
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
    └── npm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-npm-fnm`, `bruno-npm-fnm`, `depcheck-npm-fnm`, `eslint-npm-fnm`, `knip-npm-fnm`, `prettier-npm-fnm`, `stylelint-npm-fnm`, `typescript-npm-fnm`

**`npm-nvm` stack** — 8 modules (`biome-npm-nvm`, …)

```
biome-npm-nvm
    └── npm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-npm-nvm`, `bruno-npm-nvm`, `depcheck-npm-nvm`, `eslint-npm-nvm`, `knip-npm-nvm`, `prettier-npm-nvm`, `stylelint-npm-nvm`, `typescript-npm-nvm`

**`pnpm-fnm` stack** — 8 modules (`biome-pnpm-fnm`, …)

```
biome-pnpm-fnm
    └── pnpm-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-pnpm-fnm`, `bruno-pnpm-fnm`, `depcheck-pnpm-fnm`, `eslint-pnpm-fnm`, `knip-pnpm-fnm`, `prettier-pnpm-fnm`, `stylelint-pnpm-fnm`, `typescript-pnpm-fnm`

**`pnpm-nvm` stack** — 8 modules (`biome-pnpm-nvm`, …)

```
biome-pnpm-nvm
    └── pnpm-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-pnpm-nvm`, `bruno-pnpm-nvm`, `depcheck-pnpm-nvm`, `eslint-pnpm-nvm`, `knip-pnpm-nvm`, `prettier-pnpm-nvm`, `stylelint-pnpm-nvm`, `typescript-pnpm-nvm`

**`yarn-fnm` stack** — 8 modules (`biome-yarn-fnm`, …)

```
biome-yarn-fnm
    └── yarn-fnm
        ├── corepack-fnm
        │   └── fnm
        └── fnm
```

`biome-yarn-fnm`, `bruno-yarn-fnm`, `depcheck-yarn-fnm`, `eslint-yarn-fnm`, `knip-yarn-fnm`, `prettier-yarn-fnm`, `stylelint-yarn-fnm`, `typescript-yarn-fnm`

**`yarn-nvm` stack** — 8 modules (`biome-yarn-nvm`, …)

```
biome-yarn-nvm
    └── yarn-nvm
        ├── corepack-nvm
        │   └── nvm
        └── nvm
```

`biome-yarn-nvm`, `bruno-yarn-nvm`, `depcheck-yarn-nvm`, `eslint-yarn-nvm`, `knip-yarn-nvm`, `prettier-yarn-nvm`, `stylelint-yarn-nvm`, `typescript-yarn-nvm`

**`bun` stack** — 8 modules (`biome-bun`, …)

```
biome-bun
    └── bun
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

- `ansible` → `uv`
- `gh` → `jq`
- `proto` → `go`
- `python` → `uv`
- `sqlfluff` → `uv`
- `staticcheck` → `go`
- `vault` → `jq`
- `yamllint` → `uv`

### Depth 2

- `git` → `gh`

**`ansible`**

```
ansible
    └── uv
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

**`proto`**

```
proto
    └── go
```

**`python`**

```
python
    └── uv
```

**`sqlfluff`**

```
sqlfluff
    └── uv
```

**`staticcheck`**

```
staticcheck
    └── go
```

**`vault`**

```
vault
    └── jq
```

**`yamllint`**

```
yamllint
    └── uv
```

## Reverse tree

For each module, modules that depend on it (direct dependents only).

- `actionlint` — *(none)*
- `ansible` — *(none)*
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
- `corepack-fnm` ← `npm-fnm`, `pnpm-fnm`, `yarn-fnm`
- `corepack-nvm` ← `npm-nvm`, `pnpm-nvm`, `yarn-nvm`
- `depcheck-bun` — *(none)*
- `depcheck-npm-fnm` — *(none)*
- `depcheck-npm-nvm` — *(none)*
- `depcheck-pnpm-fnm` — *(none)*
- `depcheck-pnpm-nvm` — *(none)*
- `depcheck-yarn-fnm` — *(none)*
- `depcheck-yarn-nvm` — *(none)*
- `docker` — *(none)*
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
- `go` ← `proto`, `staticcheck`
- `hadolint` — *(none)*
- `jq` ← `gh`, `vault`
- `knip-bun` — *(none)*
- `knip-npm-fnm` — *(none)*
- `knip-npm-nvm` — *(none)*
- `knip-pnpm-fnm` — *(none)*
- `knip-pnpm-nvm` — *(none)*
- `knip-yarn-fnm` — *(none)*
- `knip-yarn-nvm` — *(none)*
- `npm-fnm` ← `biome-npm-fnm`, `bruno-npm-fnm`, `depcheck-npm-fnm`, `eslint-npm-fnm`, `knip-npm-fnm`, `prettier-npm-fnm`, `stylelint-npm-fnm`, `typescript-npm-fnm`
- `npm-nvm` ← `biome-npm-nvm`, `bruno-npm-nvm`, `depcheck-npm-nvm`, `eslint-npm-nvm`, `knip-npm-nvm`, `prettier-npm-nvm`, `stylelint-npm-nvm`, `typescript-npm-nvm`
- `nvm` ← `corepack-nvm`, `npm-nvm`, `pnpm-nvm`, `yarn-nvm`
- `pnpm-fnm` ← `biome-pnpm-fnm`, `bruno-pnpm-fnm`, `depcheck-pnpm-fnm`, `eslint-pnpm-fnm`, `knip-pnpm-fnm`, `prettier-pnpm-fnm`, `stylelint-pnpm-fnm`, `typescript-pnpm-fnm`
- `pnpm-nvm` ← `biome-pnpm-nvm`, `bruno-pnpm-nvm`, `depcheck-pnpm-nvm`, `eslint-pnpm-nvm`, `knip-pnpm-nvm`, `prettier-pnpm-nvm`, `stylelint-pnpm-nvm`, `typescript-pnpm-nvm`
- `prettier-bun` — *(none)*
- `prettier-npm-fnm` — *(none)*
- `prettier-npm-nvm` — *(none)*
- `prettier-pnpm-fnm` — *(none)*
- `prettier-pnpm-nvm` — *(none)*
- `prettier-yarn-fnm` — *(none)*
- `prettier-yarn-nvm` — *(none)*
- `proto` — *(none)*
- `python` — *(none)*
- `shellcheck` — *(none)*
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
- `uv` ← `ansible`, `python`, `sqlfluff`, `yamllint`
- `vault` — *(none)*
- `yamllint` — *(none)*
- `yarn-fnm` ← `biome-yarn-fnm`, `bruno-yarn-fnm`, `depcheck-yarn-fnm`, `eslint-yarn-fnm`, `knip-yarn-fnm`, `prettier-yarn-fnm`, `stylelint-yarn-fnm`, `typescript-yarn-fnm`
- `yarn-nvm` ← `biome-yarn-nvm`, `bruno-yarn-nvm`, `depcheck-yarn-nvm`, `eslint-yarn-nvm`, `knip-yarn-nvm`, `prettier-yarn-nvm`, `stylelint-yarn-nvm`, `typescript-yarn-nvm`
- `zizmor` — *(none)*
