package htmlhintnpmfnm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"config:init",
	"help",
	"install",
	"install:undo",
	"lint",
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
	tasktest.AssertModule(t, "htmlhint-npm-fnm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "htmlhint-npm-fnm",
		[]string{"lint", "TARGETS=src/**/*.html"},
		"htmlhint",
		"src/**/*.html",
	)

	tasktest.AssertDryRunContains(t, "htmlhint-npm-fnm",
		[]string{"lint", "CONFIG=.htmlhintrc"},
		"--config \".htmlhintrc\"",
	)

	tasktest.AssertDryRunContains(t, "htmlhint-npm-fnm",
		[]string{"version"},
		"htmlhint",
		"--version",
	)
}
