# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

PIP_OPTS=--no-cache-dir
setup: deps dev_deps install_project

all: setup test-unit lint

deps:
	python -m pip install -r requirements.txt ${PIP_OPTS}

dev_deps:
	python -m pip install -r requirements-dev.txt ${PIP_OPTS}

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
