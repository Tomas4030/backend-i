start:
	docker compose up --build --force-recreate

migrate:
	docker compose run --rm web poetry run python manage.py migrate

migrations:
	docker compose run --rm web poetry run python manage.py makemigrations $(app)

createsuperuser:
	docker compose run --rm web poetry run python manage.py createsuperuser

compose.collectstatic:
	docker compose exec web poetry run python manage.py collectstatic --noinput

pytest:
	docker compose run --rm web poetry run pytest

new-app:
	poetry run python manage.py startapp $(app)
	@# to execute run `make new-app app=cenas`

py3clean:
	py3clean .