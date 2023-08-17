gendiff:
	poetry run python -m gendiff.scripts.gendiff -h
	
install:
	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl
	
	
check:
	poetry run flake8 gendiff
	poetry run pytest

test-coverage:
	poetry run pytest --cov


.PHONY: install test lint check build publish
