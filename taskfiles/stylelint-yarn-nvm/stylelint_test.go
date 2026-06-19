package stylelintyarnnvm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"cache:clean",
	"ci",
	"config:init",
	"help",
	"install",
	"install:undo",
	"lint",
	"lint:fix",
	"upgrade",
	"version",
}

var publicVars = []string{
	"ALLOW_EMPTY_INPUT",
	"CACHE",
	"CONFIG",
	"EXTRA_ARGS",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "stylelint-yarn-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "stylelint-yarn-nvm",
		[]string{"lint:fix", "TARGETS=src/**/*.scss", "--", "--formatter", "verbose"},
		"yarn:exec",
		"src/**/*.scss --fix",
		"--formatter verbose",
	)
}
