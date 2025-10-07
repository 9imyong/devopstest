APP_NAME=devops-test
IMAGE=devops-test:local
REGISTRY=ghcr.io/9imyong

.PHONY: run build push kind-apply minikube-apply test

run:
	docker compose up --build

build:
	docker build -t $(IMAGE) .

push:
	docker build -t $(REGISTRY)/$(APP_NAME):latest . && \
	docker push $(REGISTRY)/$(APP_NAME):latest

minikube-apply:
	kubectl apply -f k8s/

kind-apply:
	kubectl apply -f k8s/

test:
	pytest -q
