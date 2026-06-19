package depchecknpmnvm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"ci",
	"help",
	"ignores",
	"install",
	"install:undo",
	"json",
	"lint",
	"skip-missing",
	"upgrade",
	"version",
}

var publicVars = []string{
	"EXTRA_ARGS",
	"IGNORE_PACKAGES",
	"PROJECT_PATH",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "depcheck-npm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "depcheck-npm-nvm",
		[]string{"lint", "PROJECT_PATH=packages/app", "--", "--ignores=@types/*,eslint-*"},
		"npm:exec",
		"packages/app",
		"--ignores=@types/*,eslint-*",
	)
}
