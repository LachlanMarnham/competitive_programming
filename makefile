install:
	pip install --upgrade pip
	poetry install

tests:
	pytest
