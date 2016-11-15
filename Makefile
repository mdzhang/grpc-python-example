GIT_COMMIT=$(shell git rev-parse --verify HEAD)
PROJECT_NAME=grpc_python_example
SERVICE_DEFN_DIR=./$(PROJECT_NAME)/services/definitions
SERVICE_STUB_DIR=./$(PROJECT_NAME)/services/stubs

.PHONY: build
build:
	docker build \
    --build-arg GIT_COMMIT=${GIT_COMMIT} \
    -t $(PROJECT_NAME):latest \
    -t $(PROJECT_NAME):${GIT_COMMIT} \
    .

.PHONY: clean
clean:
	py.cleanup -p .

.PHONY: down
down:
	docker-compose down

.PHONY: install
install:
	pip install -r requirements/dev.txt

.PHONY: lint
lint:
	pre-commit run pylint --all-files

.PHONY: protogen
protogen:
	python -m grpc.tools.protoc \
				 -I=$(SERVICE_DEFN_DIR) \
				 --python_out=$(SERVICE_STUB_DIR) \
				 --grpc_python_out=$(SERVICE_STUB_DIR) \
				 $(SERVICE_DEFN_DIR)/items.proto $(SERVICE_DEFN_DIR)/health.proto

# Usage: make run-text-api ARGS="check_health"
# 			 make run-text-api ARGS="get_item 1"
.PHONY: run-text-api
run-text-api:
	python -m $(PROJECT_NAME).apis.text $(ARGS)

.PHONY: run-http-api
run-http-api:
	gunicorn -b 0.0.0.0:4000 $(PROJECT_NAME).apis.http.wsgi:app

.PHONY: run-grpc-api
run-grpc-api:
	python -m $(PROJECT_NAME).apis.grpc

.PHONY: up
up:
	docker-compose up -d
