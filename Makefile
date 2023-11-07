gendiff:
	poetry run python -m gendiff.scripts.gendiff -h
	
install:
	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl

check:
	poetry check
	poetry run pytest
	poetry run flake8 gendiff

lint:
	poetry run flake8 gendiff
coverage:
	poetry run pytest --cov=gendiff --cov-report xml

update:
	poetry update
	
.PHONY: install test lint check build publish update coverage
