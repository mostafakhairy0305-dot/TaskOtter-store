#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "taskfiles"

CONFIG = {
    "fnm": {
        "includes": """includes:
  corepack:
    taskfile: ../corepack-fnm/Taskfile.yml
  fnm:
    taskfile: ../fnm/Taskfile.yml""",
        "vars": """vars:
  FNM_INSTALL_DIR: "$HOME/.local/share/fnm"
  FNM_LOAD: 'export PATH="{{.FNM_INSTALL_DIR}}:$HOME/.local/bin:$PATH"; eval "$(fnm env --shell bash)"'
  FNM_USE: >-
    {{if .NODE_VERSION}}fnm use "{{.NODE_VERSION}}"
    {{- else}}if [ -f .node-version ] || [ -f .nvmrc ]; then fnm use; fi{{end}}
  NODE_VERSION: ""
  WINDOWS_NODE_ACTIVATE: |
    fnm env --shell powershell | Out-String | Invoke-Expression
    if ($env:NODE_VERSION) {
      fnm use $env:NODE_VERSION
    } elseif ((Test-Path '.node-version') -or (Test-Path '.nvmrc')) {
      fnm use
    }""",
        "manager": "fnm",
        "unix_pre": """      - sh: >-
          test -f "{{.FNM_INSTALL_DIR}}/fnm" || command -v fnm >/dev/null 2>&1
          || test -f "$HOME/.local/bin/fnm"
        msg: 'fnm is not installed. Run: task node:setup'""",
        "win_pre": """      - sh: >-
          powershell -NoProfile -ExecutionPolicy Bypass -Command
          "if (Get-Command fnm -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }"
        msg: 'fnm is not installed or not available in PATH. Run: task node:setup'""",
        "load": "FNM_LOAD",
        "use": "FNM_USE",
        "undo_hint": "task fnm:install:undo",
    },
    "nvm": {
        "includes": """includes:
  corepack:
    taskfile: ../corepack-nvm/Taskfile.yml
  nvm:
    taskfile: ../nvm/Taskfile.yml""",
        "vars": """vars:
  NVM_LOAD: 'export NVM_DIR="$HOME/.nvm"; . "$NVM_DIR/nvm.sh"'
  NVM_USE: >-
    {{if .NODE_VERSION}}nvm use "{{.NODE_VERSION}}"
    {{- else}}if [ -f .node-version ] || [ -f .nvmrc ]; then nvm use; fi{{end}}
  NODE_VERSION: ""
  WINDOWS_NODE_ACTIVATE: |
    if ($env:NODE_VERSION) {
      nvm use $env:NODE_VERSION
    } elseif (Test-Path '.node-version') {
      $v = (Get-Content '.node-version' -Raw).Trim()
      if ($v) { nvm use $v }
    } elseif (Test-Path '.nvmrc') {
      $v = (Get-Content '.nvmrc' -Raw).Trim()
      if ($v) { nvm use $v }
    }""",
        "manager": "nvm",
        "unix_pre": """      - sh: test -s "$HOME/.nvm/nvm.sh"
        msg: 'nvm is not installed. Run: task node:setup'""",
        "win_pre": """      - sh: >-
          powershell -NoProfile -ExecutionPolicy Bypass -Command
          "if (Get-Command nvm -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }"
        msg: 'nvm is not installed or not available in PATH. Run: task node:setup'""",
        "load": "NVM_LOAD",
        "use": "NVM_USE",
        "undo_hint": "task nvm:install:undo",
    },
}


def node_setup_unix(cfg):
    m = cfg["manager"]
    return f"""  _node:setup:unix:
    internal: true
    platforms: [linux, darwin]
    set: [errexit, nounset, pipefail]
    env:
      NODE_VERSION: "{{{{.NODE_VERSION}}}}"
    preconditions:
      - sh: 'task --list-all 2>/dev/null | grep -q "{m}:node:install"'
        msg: >-
          node:setup requires the {m} taskfile included in the root Taskfile.
          Add: {m}: taskfile: taskfiles/{m}/Taskfile.yml
    cmds:
      - |
        if [ -n "$NODE_VERSION" ]; then
          task {m}:node:install VERSION="$NODE_VERSION"
        else
          task {m}:node:install
        fi"""


def node_setup_win(cfg):
    m = cfg["manager"]
    return f"""  _node:setup:windows:
    internal: true
    platforms: [windows]
    env:
      NODE_VERSION: "{{{{.NODE_VERSION}}}}"
    preconditions:
      - sh: >-
          powershell -NoProfile -ExecutionPolicy Bypass -Command
          "if ((task --list-all 2>$null | Out-String) -match '{m}:node:install')
          {{ exit 0 }} else {{ exit 1 }}"
        msg: >-
          node:setup requires the {m} taskfile included in the root Taskfile.
          Add: {m}: taskfile: taskfiles/{m}/Taskfile.yml
    cmds:
      - >-
        powershell -NoProfile -ExecutionPolicy Bypass -Command
        "if ($env:NODE_VERSION) {{ task {m}:node:install \\"VERSION=$env:NODE_VERSION\\" }}
        else {{ task {m}:node:install }}"\""""


def pm_runner_win(cfg, pm_cmd):
    return f"""    cmds:
      - >-
        powershell -NoProfile -ExecutionPolicy Bypass -Command
        "$ErrorActionPreference = 'Stop';
        $env:NODE_VERSION = '{{{{.NODE_VERSION}}}}';
        {{{{.WINDOWS_NODE_ACTIVATE}}}};
        if (-not (Get-Command corepack -ErrorAction SilentlyContinue)) {{
        Write-Error 'corepack is not available. Run: task manager:setup'; exit 1 }};
        corepack {pm_cmd} {{{{.ARGS}}}}" """


def version_win(cfg, pm_cmd):
    if pm_cmd == "npm":
        tail = "node --version; npm --version"
    else:
        tail = f"node --version; corepack {pm_cmd} --version"
    return f"""    cmds:
      - >-
        powershell -NoProfile -ExecutionPolicy Bypass -Command
        "$ErrorActionPreference = 'Stop';
        $env:NODE_VERSION = '{{{{.NODE_VERSION}}}}';
        {{{{.WINDOWS_NODE_ACTIVATE}}}};
        {tail}" """


def version_unix(cfg, pm_cmd):
    load, use = cfg["load"], cfg["use"]
    if pm_cmd == "npm":
        tail = "node --version; npm --version"
    else:
        tail = (
            "command -v corepack >/dev/null 2>&1 || "
            '{ echo "corepack is not available. Run: task manager:setup"; exit 1; }; '
            f"node --version; corepack {pm_cmd} --version"
        )
    return f"""  _version:unix:
    internal: true
    platforms: [linux, darwin]
    set: [errexit, nounset, pipefail]
    preconditions:
{cfg['unix_pre']}
    cmds:
      - >-
        bash -c '{{{{.{load}}}}}; {{{{.{use}}}}}; {tail}'"""


def transform(src: str, mgr: str, pm_cmd: str) -> str:
    cfg = CONFIG[mgr]
    internal_task = f"_{pm_cmd}"

    header = re.match(r"(---\nversion: \"3\"\n\noutput:.*?silent: true\n\n)", src, re.S).group(1)
    tasks_match = re.search(r"^tasks:\n", src, re.M)
    tasks = src[tasks_match.start():]

    replacements = [
        ("NODE_MANAGER (default: fnm)", cfg["manager"]),
        ("Set NODE_MANAGER=nvm to use nvm instead. ", ""),
        ("the node manager selected by NODE_MANAGER", cfg["manager"]),
        ("selected by NODE_MANAGER", f"via {cfg['manager']}"),
        ("Install Node.js through fnm by default or nvm when NODE_MANAGER=nvm.", f"Install Node.js through {cfg['manager']}."),
        (
            "Requires the selected node manager taskfile to be included in the root Taskfile\n      as either fnm: or nvm:. See README.md for setup instructions.",
            f"Requires the {cfg['manager']} taskfile to be included in the root Taskfile. See README.md for setup instructions.",
        ),
        (
            "Remove Node.js instead: task fnm:install:undo (fnm) or task nvm:install:undo (nvm).'",
            f"Remove Node.js instead: {cfg['undo_hint']}.'",
        ),
    ]
    for old, new in replacements:
        tasks = tasks.replace(old, new)

    tasks = re.sub(r"  _node:setup:unix:.*?(?=  _node:setup:windows:)", node_setup_unix(cfg) + "\n\n", tasks, flags=re.S)
    tasks = re.sub(rf"  _node:setup:windows:.*?(?=  {internal_task}:unix:)", node_setup_win(cfg) + "\n\n", tasks, flags=re.S)

    tasks = re.sub(
        r"      - sh: '\[ \"\{\{\.NODE_MANAGER\}\}\" = \"fnm\" \] \|\| \[ \"\{\{\.NODE_MANAGER\}\}\" = \"nvm\" \]'\n        msg: 'NODE_MANAGER must be \"fnm\" or \"nvm\", got \"\{\{\.NODE_MANAGER\}\}\"'\n",
        "",
        tasks,
    )
    tasks = re.sub(
        r"      - sh: >-\n          powershell -NoProfile -ExecutionPolicy Bypass -Command\n          \"if \('\{\{\.NODE_MANAGER\}\}' -ne 'fnm' -and '\{\{\.NODE_MANAGER\}\}' -ne 'nvm'\) \{ exit 1 \} else \{ exit 0 \}\"\n        msg: 'NODE_MANAGER must be \"fnm\" or \"nvm\", got \"\{\{\.NODE_MANAGER\}\}\"'\n",
        "",
        tasks,
    )
    tasks = re.sub(
        r"      - sh: >-\n          \{\{if eq \.NODE_MANAGER \"nvm\"\}\}test -s \"\$HOME/\.nvm/nvm\.sh\"\n          \{\{else\}\}test -f \"\{\{\.FNM_INSTALL_DIR\}\}/fnm\" \|\| command -v fnm >/dev/null 2>&1\n          \|\| test -f \"\$HOME/\.local/bin/fnm\"\{\{end\}\}\n        msg: '\"\{\{\.NODE_MANAGER\}\}\" is not installed\. Run: task node:setup'",
        cfg["unix_pre"],
        tasks,
    )
    tasks = re.sub(
        r"      - sh: >-\n          powershell -NoProfile -ExecutionPolicy Bypass -Command\n          \"if \(Get-Command \{\{\.NODE_MANAGER\}\} -ErrorAction SilentlyContinue\) \{ exit 0 \} else \{ exit 1 \}\"\n        msg: '\"\{\{\.NODE_MANAGER\}\}\" is not installed or not available in PATH\. Run: task node:setup'",
        cfg["win_pre"],
        tasks,
    )
    tasks = tasks.replace("{{.NODE_LOAD}}", "{{." + cfg["load"] + "}}")
    tasks = tasks.replace("{{.NODE_USE}}", "{{." + cfg["use"] + "}}")

    pm_win_patterns = [
        (
            rf"(  {internal_task}:windows:.*?preconditions:.*?)\n    cmds:\n"
            rf"      - \|\n        >-\n          powershell.*?\n          corepack {pm_cmd} \{{\{{\.ARGS\}}\}}\""
        ),
        (
            rf"(  {internal_task}:windows:.*?preconditions:.*?)\n    cmds:\n"
            rf"      - >-\n        powershell.*?\n        corepack {pm_cmd} \{{\{{\.ARGS\}}\}}\""
        ),
    ]
    for pattern in pm_win_patterns:
        tasks, n = re.subn(pattern, r"\1\n" + pm_runner_win(cfg, pm_cmd), tasks, flags=re.S)
        if n:
            break

    tasks = re.sub(r"  _version:unix:.*?(?=  _version:windows:)", version_unix(cfg, pm_cmd) + "\n\n", tasks, flags=re.S)
    tasks = re.sub(
        r"  _version:windows:.*?(?=  _clean:unix:)",
        f"  _version:windows:\n    internal: true\n    platforms: [windows]\n    env:\n      NODE_VERSION: \"{{{{.NODE_VERSION}}}}\"\n    preconditions:\n{cfg['win_pre']}\n"
        + version_win(cfg, pm_cmd)
        + "\n\n",
        tasks,
        flags=re.S,
    )

    return header + cfg["includes"] + "\n\n" + cfg["vars"] + "\n\n" + tasks


def main():
    for pm in ("npm", "yarn", "pnpm"):
        src = subprocess.check_output(["git", "show", f"HEAD:taskfiles/{pm}/Taskfile.yml"], text=True)
        for mgr in ("fnm", "nvm"):
            out = transform(src, mgr, pm)
            out = "\n".join(line.rstrip() for line in out.splitlines()) + "\n"
            path = ROOT / f"{pm}-{mgr}" / "Taskfile.yml"
            path.write_text(out)
            if "NODE_MANAGER" in out:
                raise SystemExit(f"NODE_MANAGER in {path}")
            if "_version:unix:" not in out:
                raise SystemExit(f"missing _version:unix in {path}")
            print(f"OK {path}")


if __name__ == "__main__":
    main()
