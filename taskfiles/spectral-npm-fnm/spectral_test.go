package spectralnpmfnm_test

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
	tasktest.AssertModule(t, "spectral-npm-fnm", publicTasks, publicVars)
}

func TestRepresentativeDryRuns(t *testing.T) {
	tasktest.AssertDryRunContains(t, "spectral-npm-fnm",
		[]string{"lint", "TARGETS=openapi.yaml", "RULESET=.spectral.yaml"},
		"spectral",
		"lint",
		"openapi.yaml",
		"--ruleset \".spectral.yaml\"",
	)

	tasktest.AssertDryRunContains(t, "spectral-npm-fnm",
		[]string{"version"},
		"spectral",
		"--version",
	)
}
