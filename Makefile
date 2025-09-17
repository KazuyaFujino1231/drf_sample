# Docker系
initialize:
	docker-compose down -v --rmi all --remove-orphans
	docker-compose build
	docker-compose up

up:
	docker-compose up

build:
	docker-compose build

# マイグレーション系
makemigrations:
	docker-compose exec backend python manage.py makemigrations

migrate:
	docker-compose exec backend python manage.py migrate

showmigrations:
	docker-compose exec backend python manage.py showmigrations

# Pythonコードフォーマット、静的解析系
poetry_run := poetry run
CHECK_DIR := ./sample/*

reformat: black isort

check:
	@echo check black
	@${poetry_run} black --check ${CHECK_DIR} --quiet
	@echo check isort
	@${poetry_run} isort --check ${CHECK_DIR} --quiet
	@echo check flake8
	@${poetry_run} flake8       ${CHECK_DIR}  # --quiet

black:
	@echo reformat black
	@${poetry_run} black ${CHECK_DIR}

isort:
	@echo reformat isort
	@${poetry_run} isort ${CHECK_DIR}

flake8:
	@echo check flake8
	@${poetry_run} flake8 ${CHECK_DIR}