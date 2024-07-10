run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@export PYTHONPATH=$(pwd) && poetry run pytest

test-matching:
	@export PYTHONPATH=$(pwd) && poetry run pytest -s -rx -k $(K) --pdb store ./tests/
