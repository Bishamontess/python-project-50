gendiff:
		poetry run python -m gendiff.scripts.gendiff -h

install:
		poetry install

selfcheck:
		poetry check

check: selfcheck test lint

test:
		cd tests/
		poetry run pytest

lint:
		poetry run flake8 gendiff

coverage:
		poetry run pytest --cov=gendiff --cov-report xml

build:
		poetry build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

full-install: install build package-install

.PHONY: install test lint check build update coverage selfcheck check
