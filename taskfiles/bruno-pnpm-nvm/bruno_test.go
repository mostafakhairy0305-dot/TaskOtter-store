package brunopnpmnvm_test

import (
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
)

var publicTasks = []string{
	"ci",
	"help",
	"install",
	"install:undo",
	"run",
	"upgrade",
	"version",
}

var publicVars = []string{
	"COLLECTION",
	"ENV",
	"EXTRA_ARGS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "bruno-pnpm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "bruno-pnpm-nvm",
		[]string{"run"},
		"pnpm:exec",
		`run .`,
	)
}
