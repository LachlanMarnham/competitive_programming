install:
	pip install --upgrade pip
	poetry install

tests:
	pytest

check-style:
	isort . -c
	black .
	flake8

isort:
	isort .
