# make run
.PHONY: run
run:
	python3 src/manage.py runserver

# make check
.PHONY: check
check:
	python3 -m flake8 . && python3 -m black --check . && python3 -m isort --check .

# make fix
.PHONY: fix
fix:
	python3 -m ruff --fix . && python3 -m black . && python3 -m isort .

# make makemigrations
.PHONY: makemigrations
makemigrations:
	python3 src/manage.py makemigrations

# make migrate
.PHONY: migrate
migrate:
	python3 src/manage.py migrate