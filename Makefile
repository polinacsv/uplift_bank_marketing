.PHONY: clean build install test update-requirements setup

clean:
	@echo "Cleaning build files and caches..."
	rm -rf build/ dist/ *.egg-info
	rm -rf src/uplift_bank_marketing/*.egg-info
	rm -rf src/uplift_bank_marketing/__pycache__

build:
	@echo "Building the project..."
	mkdir -p build/egg-info  # Ensure the egg-info directory exists
	python setup.py clean --all
	python setup.py build

install:
	@echo "Installing the project in editable mode..."
	pip install -e .

test:
	@echo "Running tests..."
	python -m unittest discover -s tests

update-requirements:
	@echo "Updating requirements.txt..."
	pip freeze | grep -v uplift_bank_marketing > requirements.txt

setup: clean build install
	@echo "Project setup complete!"


data:
	@echo "Loading and saving Bank Marketing data..."
	python -c "from uplift_bank_marketing.data.load_data import load_data; load_data()"

setup-full: clean build install data
	@echo "Project fully set up, data loaded!"

# Setup Git pre-commit hook for auto-clearing Jupyter Notebook outputs
install-precommit:
	@echo "#!/bin/bash" > .git/hooks/pre-commit
	@echo "echo 'Clearing Jupyter Notebook outputs...'" >> .git/hooks/pre-commit
	@echo "nbstripout --install" >> .git/hooks/pre-commit
	@echo "find . -name '*.ipynb' -exec nbstripout {} \;" >> .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "Pre-commit hook for clearing notebook outputs installed."

# Clear notebook outputs manually
clear-notebook-output:
	find . -name '*.ipynb' -exec nbstripout {} \;