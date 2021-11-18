# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: setup test-unit lint

upgrade_pip:
        python -m pip install --upgrade pip

deps:
	python -m pip install -r requirements.txt

dev_deps:
	python -m pip install -r requirements-dev.txt

install_project:
	python -m pip install -e .

test: test-unit test-int

test-unit:
	python -m pytest ibm-whcs-sdk/annotator-for-clinical-data/tests/unit
	python -m pytest ibm-whcs-sdk/insights-for-medical-literature/tests/unit

test-int:
	python -m pytest ibm-whcs-sdk/annotator-for-clinical-data/tests/integration
	python -m pytest ibm-whcs-sdk/insights-for-medical-literature/tests/integration

lint:
	./pylint.sh
