package spectralpnpmfnm_test

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
	tasktest.AssertModule(t, "spectral-pnpm-fnm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "spectral-pnpm-fnm",
		[]string{"lint", "TARGETS=openapi.yaml"},
		"pnpm:exec",
		"spectral",
		"lint",
		"openapi.yaml",
	)

	tasktest.AssertDryRunContains(t, "spectral-pnpm-fnm",
		[]string{"version"},
		"spectral",
		"--version",
	)
}
