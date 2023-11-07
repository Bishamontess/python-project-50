gendiff:
		poetry run python -m gendiff.scripts.gendiff -h

install:
		poetry install

selfcheck:
		poetry check

check: selfcheck test lint

test:
		poetry run pytest

lint:
		poetry run flake8 gendiff

coverage:
		poetry run pytest --cov=gendiff --cov-report xml

update:
		poetry update

.PHONY: install test lint check build update coverage selfcheck
