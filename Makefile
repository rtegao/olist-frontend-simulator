install:
	poetry install

black:
	black frontend_simulator

isort:
	isort --profile black frontend_simulator

type_hinting_checker:
	flake8 frontend_simulator

linter:
	pylint frontend_simulator

format: black isort type_hinting_checker linter


init-kafka:
	docker-compose up init-kafka

control-center-interface:
	docker-compose up control-center

run:
	poetry run python app.py