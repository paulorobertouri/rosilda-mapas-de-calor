SHELL := /bin/bash

.PHONY: help install build run test e2e e2e-evidence lint format clean

help:
	@echo "Available commands:"
	@echo "  install      Install Python dependencies with uv"
	@echo "  build        Syntax-check Python sources"
	@echo "  run          Generate heatmap outputs"
	@echo "  test         Run all tests with pytest"
	@echo "  e2e          Run e2e (generates outputs and tests)"
	@echo "  e2e-evidence Run e2e and save output images as evidence"
	@echo "  lint         Lint code with ruff"
	@echo "  format       Format code with ruff"
	@echo "  clean        Remove build and test artifacts"

install:
	./scripts/install.sh

build:
	./scripts/build.sh

run:
	./scripts/run.sh

test:
	./scripts/test.sh

e2e:
	./scripts/e2e.sh test

e2e-evidence:
	./scripts/e2e.sh evidence

lint:
	./scripts/lint.sh

format:
	./scripts/format.sh

clean:
	./scripts/clean.sh
