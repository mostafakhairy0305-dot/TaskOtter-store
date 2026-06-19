package eslintpnpmnvm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"cache:clean",
	"ci",
	"config:init",
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
	"CACHE",
	"CONFIG",
	"EXTRA_ARGS",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "eslint-pnpm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "eslint-pnpm-nvm",
		[]string{"lint", "TARGETS=src test", "--", "--quiet"},
		"pnpm:exec",
		"--cache --cache-location .cache/eslint/",
		"src test",
		"--quiet",
	)
}
