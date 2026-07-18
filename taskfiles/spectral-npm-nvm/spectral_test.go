package spectralnpmnvm_test

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
	"SPECTRAL_LINT_SKIP_PATTERN",
	"EXTRA_ARGS",
	"RULESET",
	"TARGETS",
	"VERSION",
}

func TestTaskfileModuleContract(t *testing.T) {
	tasktest.AssertModule(t, "spectral-npm-nvm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "spectral-npm-nvm",
		[]string{"lint", "TARGETS=openapi.yaml"},
		"spectral",
		"lint",
		"openapi.yaml",
	)

	tasktest.AssertDryRunContains(t, "spectral-npm-nvm",
		[]string{"version"},
		"spectral",
		"--version",
	)
}
