#!/usr/bin/env python3
"""Generate per-PM variants of JS tool taskfiles (eslint, prettier, etc.)."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKFILES = ROOT / "taskfiles"

TOOLS = ["eslint", "prettier", "biome", "bruno", "depcheck", "knip", "stylelint", "typescript"]

PM_CONFIGS = [
    {"suffix": "npm-fnm", "pm": "npm", "taskfile": "../npm-fnm/Taskfile.yml", "dep": "npm-fnm"},
    {"suffix": "yarn-fnm", "pm": "yarn", "taskfile": "../yarn-fnm/Taskfile.yml", "dep": "yarn-fnm"},
    {"suffix": "pnpm-fnm", "pm": "pnpm", "taskfile": "../pnpm-fnm/Taskfile.yml", "dep": "pnpm-fnm"},
    {"suffix": "npm-nvm", "pm": "npm", "taskfile": "../npm-nvm/Taskfile.yml", "dep": "npm-nvm"},
    {"suffix": "yarn-nvm", "pm": "yarn", "taskfile": "../yarn-nvm/Taskfile.yml", "dep": "yarn-nvm"},
    {"suffix": "pnpm-nvm", "pm": "pnpm", "taskfile": "../pnpm-nvm/Taskfile.yml", "dep": "pnpm-nvm"},
    {"suffix": "bun", "pm": "bun", "taskfile": "../bun/Taskfile.yml", "dep": "bun"},
]

EXEC_IGNORE_TASK = """  _exec:ignore:
    internal: true
    desc: Execute a local project binary and include an ignore file when present
    requires:
      vars: [BINARY]
    vars:
      IGNORE_FLAG: "--ignore-path"
      _IGNORE_ARGS:
        sh: |
          if [ -n "{{{{.IGNORE_PATH}}}}" ] && [ -f "{{{{.IGNORE_PATH}}}}" ]; then
            echo "{{{{.IGNORE_FLAG}}}} {{{{.IGNORE_PATH}}}}"
          fi
    cmds:
      - task: {pm}:exec
        vars:
          BINARY: "{{{{.BINARY}}}}"
          ARGS: "{{{{.ARGS}}}} {{{{._IGNORE_ARGS}}}}"
          EXTRA_ARGS: "{{{{.EXTRA_ARGS}}}}{{{{if .CLI_ARGS}}}} {{{{.CLI_ARGS}}}}{{{{end}}}}"
"""


def go_package(variant: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", "", variant) + "_test"


def transform_taskfile(content: str, pm: str, taskfile_path: str, tool: str) -> str:
    content = re.sub(
        r"includes:\n  js:\n    taskfile: \.\./js-pm/Taskfile\.yml\n",
        f"includes:\n  {pm}:\n    taskfile: {taskfile_path}\n",
        content,
    )

    uses_exec_ignore = "js:exec:ignore" in content

    content = content.replace("js:_install-packages", f"{pm}:add")
    content = content.replace("js:remove", f"{pm}:remove")
    content = content.replace("js:exec:ignore", "_exec:ignore")
    content = content.replace("js:exec", f"{pm}:exec")

    content = re.sub(
        r"\n          PM: \"\{\{if \.PM_OVERRIDE\}\}\{\{\.PM_OVERRIDE\}\}\{\{else\}\}\{\{\.PM\}\}\{\{end\}\}\"\n",
        "\n",
        content,
    )
    content = re.sub(r"\n  PM: \"\"\n", "\n", content)

    old_exec_vars = (
        '          EXTRA_ARGS: "{{if .EXTRA_ARGS_OVERRIDE}}{{.EXTRA_ARGS_OVERRIDE}}'
        '{{else}}{{.EXTRA_ARGS}}{{end}}"\n'
        '          CLI_ARGS: "{{.CLI_ARGS}}"'
    )
    new_exec_vars = (
        '          EXTRA_ARGS: "{{if .EXTRA_ARGS_OVERRIDE}}{{.EXTRA_ARGS_OVERRIDE}}'
        '{{else}}{{.EXTRA_ARGS}}{{end}}{{if .CLI_ARGS}} {{.CLI_ARGS}}{{end}}"'
    )
    content = content.replace(old_exec_vars, new_exec_vars)

    old_multiline = (
        "          EXTRA_ARGS: >-\n"
        "            {{if .EXTRA_ARGS_OVERRIDE}}{{.EXTRA_ARGS_OVERRIDE}}\n"
        "            {{else}}{{if .EXTRA_ARGS}}{{.EXTRA_ARGS}}{{end}}{{end}}\n"
        '          CLI_ARGS: "{{.CLI_ARGS}}"'
    )
    new_multiline = (
        "          EXTRA_ARGS: >-\n"
        "            {{if .EXTRA_ARGS_OVERRIDE}}{{.EXTRA_ARGS_OVERRIDE}}\n"
        "            {{else}}{{if .EXTRA_ARGS}}{{.EXTRA_ARGS}}{{end}}{{end}}{{if .CLI_ARGS}} {{.CLI_ARGS}}{{end}}"
    )
    content = content.replace(old_multiline, new_multiline)

    if uses_exec_ignore and "  _exec:ignore:" not in content:
        content = content.rstrip() + "\n\n" + EXEC_IGNORE_TASK.format(pm=pm) + "\n"

    if tool == "typescript" and "_install:windows:" in content:
        win_install = f"""  _install:windows:
    internal: true
    platforms: [windows]
    dir: "{{{{.USER_WORKING_DIR}}}}"
    env:
      TS_VERSION: "{{{{.VERSION}}}}"
    preconditions:
      - sh: >-
          powershell -NoProfile -ExecutionPolicy Bypass -Command
          "if (Test-Path '{{{{.USER_WORKING_DIR}}}}\\\\package.json') {{ exit 0 }} else {{ exit 1 }}"
        msg: "package.json not found. Run this task from the Node.js project root."
    cmds:
      - task: {pm}:add
        vars:
          PACKAGES: >-
            {{{{if .VERSION}}}}typescript@{{{{.VERSION}}}} tsx @types/node{{{{else}}}}typescript tsx @types/node{{{{end}}}}

"""
        content = re.sub(
            r"  _install:windows:.*?(?=  _version:unix:)",
            lambda _: win_install,
            content,
            flags=re.S,
        )

    return "\n".join(line.rstrip() for line in content.splitlines()) + "\n"


def transform_readme(content: str, tool: str, variant: str, pm: str, suffix: str, dep: str) -> str:
    title = tool.capitalize() if tool != "eslint" else "ESLint"
    if tool == "typescript":
        title = "TypeScript"
    elif tool == "biome":
        title = "Biome"
    elif tool == "bruno":
        title = "Bruno"
    elif tool == "depcheck":
        title = "Depcheck"
    elif tool == "knip":
        title = "Knip"
    elif tool == "prettier":
        title = "Prettier"
    elif tool == "stylelint":
        title = "Stylelint"

    stack = f"`{dep}`" if suffix == "bun" else f"`{suffix}` stack (`{dep}`)"

    content = re.sub(
        rf"# {re.escape(title)} Taskfile Public Tasks",
        f"# {title} Taskfile ({suffix}) Public Tasks",
        content,
        count=1,
    )
    content = re.sub(
        r"shared `js-pm` helper\.?\n?",
        "",
        content,
    )
    content = re.sub(
        r"and uses `js-pm` for package-manager detection and binary execution\.\n?",
        "",
        content,
    )
    content = re.sub(
        r"and uses the shared `js-pm` helper for local binary[^\n]*\n?",
        "",
        content,
    )
    content = re.sub(
        r"and delegates package-manager behavior to the\nshared `js-pm` helper\.\n?",
        "",
        content,
    )
    content = re.sub(
        r"and keeps package-manager selection consistent with the shared\n`js-pm` helper\.\n?",
        f"This variant uses the {stack} package manager.\n\n",
        content,
    )
    content = re.sub(
        r"## Variables\n\n`PM` defaults to lockfile detection through `js-pm`[^\n]*\n\n",
        "## Setup\n\n",
        content,
    )
    content = re.sub(
        r"`PM` defaults to lockfile detection through `js-pm`[^\n]*\n\n",
        "",
        content,
    )
    content = re.sub(
        r"Optional `PM`(?:, `)?",
        "Optional `",
        content,
    )
    content = re.sub(
        r"; optional `PM`(?:, `)?",
        "; optional `",
        content,
    )
    content = re.sub(
        r"\| Optional `PM` \|",
        "| — |",
        content,
    )

    setup = f"""```yaml
includes:
  {pm}:
    taskfile: taskfiles/{dep}/Taskfile.yml
  {tool}:
    taskfile: taskfiles/{variant}/Taskfile.yml
```

"""
    if "## Setup" not in content:
        content = content.replace("## Public Tasks\n", f"## Setup\n\n{setup}## Public Tasks\n", 1)

    content = re.sub(r"task {tool}:[^\n]* PM=[^\n]*\n", "", content)
    content = content.replace(f"task {tool}:", f"task {tool}:")

    return content


def transform_standard_test(content: str, tool: str, variant: str, pm: str, suffix: str) -> str:
    pkg = go_package(variant)
    content = content.replace(f"package {tool}_test", f"package {pkg}")
    content = content.replace(f'"{tool}"', f'"{variant}"')

    content = re.sub(r'\n\t"PM",\n', "\n", content)

    if "TestRepresentativeDryRuns" in content:
        dry_block = extract_dry_run_for_pm(content, pm, suffix)
        content = re.sub(
            r"func TestRepresentativeDryRuns\(t \*testing\.T\) \{.*?\n\}",
            dry_block,
            content,
            flags=re.S,
        )

    return content


def extract_dry_run_for_pm(content: str, pm: str, suffix: str) -> str:
    pm_patterns = {
        "pnpm": ["PM=pnpm", "js:pnpm:exec"],
        "yarn": ["PM=yarn", "js:yarn:exec"],
        "npm": ["PM=npm", "js:npm:exec"],
        "bun": ["PM=bun", "js:bun:exec"],
    }
    target_pm = pm
    for key, (pm_arg, exec_token) in pm_patterns.items():
        if key == target_pm:
            block_start = content.find("func TestRepresentativeDryRuns")
            block = content[block_start:]
            tests = []
            pos = 0
            while True:
                idx = block.find("tasktest.AssertDryRunContains", pos)
                if idx == -1:
                    break
                end = block.find("\n\t)", idx)
                if end == -1:
                    end = block.find("\n)", idx)
                test = block[idx : end + 1]
                if pm_arg in test:
                    test = test.replace(exec_token, f"{pm}:exec")
                    test = re.sub(r', "PM=[^"]+"', "", test)
                    test = re.sub(r'"PM=[^"]+", ', "", test)
                    tests.append(test)
                pos = end + 1

            if not tests and "eslint" in content:
                tests = [f'''\ttasktest.AssertDryRunContains(t, "{content.split('package ')[1].split('_test')[0] if False else variant}",
\t\t[]string{{"lint", "TARGETS=src test", "--", "--quiet"}},
\t\t"{pm}:exec",
\t\t"--cache --cache-location .cache/eslint/",
\t\t"src test",
\t\t"--quiet",
\t)''']

            body = "\n\n".join(tests) if tests else "\t// dry-run covered by module contract"
            return f"func TestRepresentativeDryRuns(t *testing.T) {{\n{body}\n}}"
    return "func TestRepresentativeDryRuns(t *testing.T) {\n\t// covered by module contract\n}"


def transform_standard_test_v2(content: str, tool: str, variant: str, pm: str) -> str:
    pkg = go_package(variant)
    content = content.replace(f"package {tool}_test", f"package {pkg}")
    content = content.replace(f'tasktest.AssertModule(t, "{tool}"', f'tasktest.AssertModule(t, "{variant}"')
    content = content.replace(f'tasktest.AssertDryRunContains(t, "{tool}"', f'tasktest.AssertDryRunContains(t, "{variant}"')
    content = re.sub(r'\n\t"PM",\n', "\n", content)

    pm_arg = f"PM={pm}"
    if "TestRepresentativeDryRuns" in content:
        lines = content.splitlines()
        new_lines = []
        in_test = False
        skip_until_close = False
        paren_depth = 0
        kept_tests = []
        current_test = []

        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("func TestRepresentativeDryRuns"):
                in_test = True
                i += 1
                continue
            if in_test:
                if line.startswith("func ") and not line.startswith("func TestRepresentativeDryRuns"):
                    break
                if "tasktest.AssertDryRunContains" in line:
                    test_lines = [line]
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith(")"):
                        test_lines.append(lines[i])
                        i += 1
                    if i < len(lines):
                        test_lines.append(lines[i])
                    block = "\n".join(test_lines)
                    if pm_arg in block or (pm == "bun" and "PM=bun" in block):
                        block = block.replace("js:pnpm:exec", f"{pm}:exec")
                        block = block.replace("js:yarn:exec", f"{pm}:exec")
                        block = block.replace("js:npm:exec", f"{pm}:exec")
                        block = block.replace("js:bun:exec", f"{pm}:exec")
                        block = re.sub(r', "PM=[^"]+"', "", block)
                        block = re.sub(r'"PM=[^"]+", ', "", block)
                        block = block.replace(f'"{tool}"', f'"{variant}"')
                        kept_tests.append(block)
                    continue
                i += 1
                continue
            new_lines.append(line)
            i += 1

        insert_at = len(new_lines)
        for j, line in enumerate(new_lines):
            if line.startswith("func TestRepresentativeDryRuns"):
                insert_at = j
                break

        dry_func = ["func TestRepresentativeDryRuns(t *testing.T) {"]
        if kept_tests:
            dry_func.extend(kept_tests)
        else:
            dry_func.append("\t// covered by module contract")
        dry_func.append("}")
        new_lines = new_lines[:insert_at] + dry_func + new_lines[insert_at + 1 :]
        content = "\n".join(new_lines) + "\n"

    return content


def copy_typescript_test(content: str, variant: str) -> str:
    pkg = go_package(variant)
    return content.replace("package typescript_test", f"package {pkg}")


def generate_variant(tool: str, cfg: dict) -> None:
    suffix = cfg["suffix"]
    pm = cfg["pm"]
    variant = f"{tool}-{suffix}"
    out_dir = TASKFILES / variant
    out_dir.mkdir(exist_ok=True)

    src_dir = TASKFILES / tool
    taskfile = (src_dir / "Taskfile.yml").read_text()
    taskfile = transform_taskfile(taskfile, pm, cfg["taskfile"], tool)
    (out_dir / "Taskfile.yml").write_text(taskfile)

    readme_path = src_dir / "README.md"
    if readme_path.exists():
        readme = transform_readme(readme_path.read_text(), tool, variant, pm, suffix, cfg["dep"])
        (out_dir / "README.md").write_text(readme)

    test_name = f"{tool}_test.go"
    test_src = src_dir / test_name
    if test_src.exists():
        test_content = test_src.read_text()
        if tool == "typescript":
            test_content = copy_typescript_test(test_content, variant)
        else:
            test_content = transform_standard_test_v2(test_content, tool, variant, pm)
        (out_dir / test_name).write_text(test_content)


def generate_deps_entries() -> dict[str, list[str]]:
    entries: dict[str, list[str]] = {}
    for tool in TOOLS:
        for cfg in PM_CONFIGS:
            variant = f"{tool}-{cfg['suffix']}"
            entries[variant] = [cfg["dep"]]
    return entries


def main() -> None:
    for tool in TOOLS:
        if not (TASKFILES / tool / "Taskfile.yml").exists():
            raise SystemExit(f"missing source tool: {tool}")
        for cfg in PM_CONFIGS:
            generate_variant(tool, cfg)
            print(f"OK taskfiles/{tool}-{cfg['suffix']}/")

    print(f"Generated {len(TOOLS) * len(PM_CONFIGS)} variants")


if __name__ == "__main__":
    main()
