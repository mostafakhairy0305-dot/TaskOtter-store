package eslintnpmnvm_test

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
	tasktest.AssertModule(t, "eslint-npm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "eslint-npm-nvm",
		[]string{"config:init"},
		"npm:exec",
		"--init",
	)
}
