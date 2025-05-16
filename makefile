.PHONY: app app-linter app-linter-fix

app:
	docker-compose up --build

app-linter:
	docker-compose run --rm api bash -c "flake8 app/ && black --check app/ && isort --check-only app/"

app-linter-fix:
	docker-compose run --rm api bash -c "flake8 app/ || true && black app/ && isort app/"

tests:
	docker-compose run --rm test bash -c "export PYTHONPATH=/app && pytest"



