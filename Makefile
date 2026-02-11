.PHONY: build test lint install clean help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## Build the package
	pip install -e .

test: ## Run tests
	pytest -v --tb=short

lint: ## Run linter
	ruff check .

install: ## Install for production
	pip install .

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info __pycache__ .pytest_cache

ci: lint test ## Run CI checks
