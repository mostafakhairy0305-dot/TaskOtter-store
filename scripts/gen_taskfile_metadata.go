// Command gen_taskfile_metadata writes the public task metadata for every
// TaskOtter module.
package main

import (
	"bytes"
	"fmt"
	"os"
	"path/filepath"
	"slices"
	"strings"

	"gopkg.in/yaml.v3"
)

const metadataSchema = "taskotter.dev/taskfile-metadata/v1"

type taskfile struct {
	Tasks map[string]task `yaml:"tasks"`
}

type task struct {
	Internal bool `yaml:"internal"`
}

type metadata struct {
	Schema        string   `yaml:"schema"`
	Module        string   `yaml:"module"`
	Taskfile      string   `yaml:"taskfile"`
	ExportedTasks []string `yaml:"exported_tasks"`
}

func main() {
	paths, err := filepath.Glob(filepath.Join("taskfiles", "*", "Taskfile.yml"))
	if err != nil {
		fatalf("find module Taskfiles: %v", err)
	}
	if len(paths) == 0 {
		fatalf("no module Taskfiles found; run this command from the repository root")
	}

	for _, path := range paths {
		if err := generate(path); err != nil {
			fatalf("generate metadata for %s: %v", path, err)
		}
	}

	fmt.Printf("generated metadata for %d modules\n", len(paths))
}

func generate(path string) error {
	content, err := os.ReadFile(path)
	if err != nil {
		return fmt.Errorf("read Taskfile: %w", err)
	}

	var source taskfile
	if err := yaml.Unmarshal(content, &source); err != nil {
		return fmt.Errorf("parse Taskfile: %w", err)
	}

	tasks := make([]string, 0, len(source.Tasks))
	for name, task := range source.Tasks {
		if name == "default" || strings.HasPrefix(name, "_") || task.Internal {
			continue
		}
		tasks = append(tasks, name)
	}
	slices.Sort(tasks)

	document := metadata{
		Schema:        metadataSchema,
		Module:        filepath.Base(filepath.Dir(path)),
		Taskfile:      filepath.Base(path),
		ExportedTasks: tasks,
	}

	var output bytes.Buffer
	output.WriteString("---\n")
	encoder := yaml.NewEncoder(&output)
	encoder.SetIndent(2)
	if err := encoder.Encode(document); err != nil {
		return fmt.Errorf("encode metadata: %w", err)
	}
	if err := encoder.Close(); err != nil {
		return fmt.Errorf("close metadata encoder: %w", err)
	}

	metadataPath := filepath.Join(filepath.Dir(path), "metadata.yml")
	if err := os.WriteFile(metadataPath, output.Bytes(), 0o644); err != nil {
		return fmt.Errorf("write %s: %w", metadataPath, err)
	}
	return nil
}

func fatalf(format string, args ...any) {
	fmt.Fprintf(os.Stderr, format+"\n", args...)
	os.Exit(1)
}
