install:
	pip install --upgrade pip
	poetry install

tests:
	pytest

check-style:
	python format_sql.py ./SQL
	isort . -c
	black .
	flake8

isort:
	isort .

add:
	mkdir $(dir)
	touch $(dir)/__init__.py
	touch $(dir)/test.py
	touch $(dir)/solution.py