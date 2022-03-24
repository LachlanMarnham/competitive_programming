install:
	pip install --upgrade pip
	poetry install

tests:
	pytest

check-style:
	flake8

isort:
	isort .
