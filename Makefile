all: install test run

install:
	poetry lock --no-update
	poetry install --with=dev,test

kill: kill-api kill-app

kill-api:
	kill -9 `lsof -t -i:8000`

kill-app:
	kill -9 `lsof -t -i:8501`

lint:
	poetry run black .
	poetry run mypy .
	poetry run pylint api/ app/

run: 
	make run-api & make run-app

run-api:
	cd api && poetry run uvicorn main:api --reload

run-app:
	cd app && poetry run streamlit run main.py

setup-env-variables:
	cp app/.streamlit/secrets.example.toml app/.streamlit/secrets.toml

test: test-api test-app

test-api:
	poetry run pytest api/tests/

test-app:
	poetry run pytest app/tests/