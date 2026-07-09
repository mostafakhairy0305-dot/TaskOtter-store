package spectralpnpmnvm_test

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
	"EXTRA_ARGS",
	"RULESET",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "spectral-pnpm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "spectral-pnpm-nvm",
		[]string{"lint", "TARGETS=openapi.yaml"},
		"pnpm:exec",
		"spectral",
		"lint",
		"openapi.yaml",
	)

	tasktest.AssertDryRunContains(t, "spectral-pnpm-nvm",
		[]string{"version"},
		"spectral",
		"--version",
	)
}
