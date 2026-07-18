package taskfiles_test

import (
	"os"
	"path/filepath"
	"slices"
	"strings"
	"testing"

	"github.com/mostafakhairy0305-dot/TaskOtter/internal/tasktest"
	"gopkg.in/yaml.v3"
)

const metadataSchema = "taskotter.dev/taskfile-metadata/v1"

type moduleMetadata struct {
	Schema        string   `yaml:"schema"`
	Module        string   `yaml:"module"`
	Taskfile      string   `yaml:"taskfile"`
	ExportedTasks []string `yaml:"exported_tasks"`
}

func TestModuleMetadataListsEveryExportedTask(t *testing.T) {
	root := tasktest.RepoRoot(t)
	taskfilePaths, err := filepath.Glob(filepath.Join(root, "taskfiles", "*", "Taskfile.yml"))
	if err != nil {
		t.Fatalf("find module Taskfiles: %v", err)
	}
	if len(taskfilePaths) == 0 {
		t.Fatal("no module Taskfiles found")
	}

	for _, taskfilePath := range taskfilePaths {
		module := filepath.Base(filepath.Dir(taskfilePath))
		t.Run(module, func(t *testing.T) {
			metadataPath := filepath.Join(filepath.Dir(taskfilePath), "metadata.yml")
			content, err := os.ReadFile(metadataPath)
			if err != nil {
				t.Fatalf("read metadata.yml: %v; regenerate with go run ./scripts/gen_taskfile_metadata.go", err)
			}
			if strings.Contains(string(content), "\r\n") {
				t.Fatal("metadata.yml must use LF line endings")
			}
			if strings.TrimRight(string(content), " \t\r\n") != strings.TrimRight(string(content), "\r\n") {
				t.Fatal("metadata.yml has trailing whitespace")
			}

			var metadata moduleMetadata
			if err := yaml.Unmarshal(content, &metadata); err != nil {
				t.Fatalf("parse metadata.yml: %v", err)
			}
			if metadata.Schema != metadataSchema {
				t.Errorf("schema = %q, want %q", metadata.Schema, metadataSchema)
			}
			if metadata.Module != module {
				t.Errorf("module = %q, want %q", metadata.Module, module)
			}
			if metadata.Taskfile != "Taskfile.yml" {
				t.Errorf("taskfile = %q, want %q", metadata.Taskfile, "Taskfile.yml")
			}
			if !slices.IsSorted(metadata.ExportedTasks) {
				t.Errorf("exported_tasks must be sorted: %v", metadata.ExportedTasks)
			}
			for i := 1; i < len(metadata.ExportedTasks); i++ {
				if metadata.ExportedTasks[i] == metadata.ExportedTasks[i-1] {
					t.Errorf("exported_tasks contains duplicate %q", metadata.ExportedTasks[i])
				}
			}

			taskfile := tasktest.LoadTaskfile(t, module)
			expected := make([]string, 0, len(taskfile.Tasks))
			for name, task := range taskfile.Tasks {
				if name == "default" || strings.HasPrefix(name, "_") || task.Internal {
					continue
				}
				expected = append(expected, name)
			}
			slices.Sort(expected)
			if !slices.Equal(metadata.ExportedTasks, expected) {
				t.Fatalf(
					"exported task drift\nmetadata: %v\ntaskfile: %v\nregenerate with go run ./scripts/gen_taskfile_metadata.go",
					metadata.ExportedTasks,
					expected,
				)
			}
		})
	}
}
