SHELL=/bin/bash
.DEFAULT_GOAL=setup
CURRENTDIR=$(shell dirname `pwd`)

ifneq (,$(wildcard ./.env))
include .env
export
endif

setup: requirements.txt
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -r requirements.txt

	@echo ""
	@echo "Creating .env file, don't forget to change values according to your environment"
	@test -f .env || cp .env.example .env

	@sleep 2
	@echo ""
	@echo "Change .env values and execute make migrate to apply database changes."

run:
	. .venv/bin/activate; FLASK_APP=src flask run --debug

add_dep: .venv
	. .venv/bin/activate; pip install $(dep) && pip freeze | grep -v "pkg-resources" > requirements.txt

rm_dep: .venv
	. .venv/bin/activate; pip uninstall $(dep) && pip freeze | grep -v "pkg-resources" > requirements.txt -y

# Build docker image to test locally
docker_build:
	docker build \
		--build-arg DATABASE_MIGRATION_URL=${DATABASE_MIGRATION_URL} \
		--build-arg STORAGE_BUCKET=${STORAGE_BUCKET} \
		--build-arg PROJECT=${PROJECT} \
		-t <SERVICE> .

# Run docker image already built locally
docker_run:
	docker run -p 5000:5000 \
	 <SERVICE>:latest

# Compile docker images and run locally
docker_compile:
	make docker_build
	make docker_run