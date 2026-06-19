package biomepnpmfnm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"cache:clean",
	"check",
	"check:write",
	"ci",
	"config:init",
	"fix",
	"fmt",
	"fmt:check",
	"help",
	"init",
	"install",
	"install:undo",
	"lint",
	"lint:fix",
	"upgrade",
	"version",
}

var publicVars = []string{
	"CONFIG",
	"EXTRA_ARGS",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "biome-pnpm-fnm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "biome-pnpm-fnm",
		[]string{"fmt", "--", "--no-errors-on-unmatched"},
		"pnpm:exec",
		"format --write",
		"--no-errors-on-unmatched",
	)
}
