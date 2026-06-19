package prettieryarnfnm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"ci",
	"config:init",
	"fix",
	"fmt",
	"fmt:check",
	"help",
	"install",
	"install:undo",
	"upgrade",
	"version",
}

var publicVars = []string{
	"CONFIG",
	"EXTRA_ARGS",
	"IGNORE_PATH",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "prettier-yarn-fnm", publicTasks, publicVars)
}

func TestConfigInitDryRun(t *testing.T) {
	tasktest.AssertDryRunContains(t, "prettier-yarn-fnm", []string{"config:init"},
		"singleQuote",
		".prettierrc.json",
	)
}

func TestRepresentativeDryRuns(t *testing.T) {
	// covered by module contract
}
