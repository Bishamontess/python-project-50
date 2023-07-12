gendiff:
	poetry run python -m gendiff.scripts.gendiff -h
build:
	poetry build
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
	
lint:
test:
test-coverage:

.PHONY: install test lint selfcheck check build publish
