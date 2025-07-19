PROTO_DIR=proto
PROTO_FILES=$(wildcard $(PROTO_DIR)/*.proto)
SVC2_DIR=svc-2
SVC2_OUT=$(SVC2_DIR)/pb

.PHONY: all proto clean run-server run-client run-services stop-services docker-build docker-up docker-down docker-logs

proto:
	mkdir -p $(SVC2_OUT)
	protoc --go_out=$(SVC2_OUT) --go-grpc_out=$(SVC2_OUT) -I $(PROTO_DIR) $(PROTO_FILES)

clean:
	rm -rf $(SVC2_OUT)

run-server:
	cd svc-2 && go run main.go

run-client:
	cd svc-1 && pnpm run dev

run-services:
	@echo "Starting gRPC server..."
	cd svc-2 && go run main.go &
	@echo "Waiting for server to start..."
	sleep 2
	@echo "Running client..."
	cd svc-1 && pnpm run dev

stop-services:
	@echo "Stopping background processes..."
	pkill -f "go run main.go" || true

# Docker commands
docker-build:
	@echo "Building Docker images..."
	docker compose build

docker-up:
	@echo "Starting services with Docker Compose..."
	docker compose up

docker-up-detached:
	@echo "Starting services with Docker Compose (detached)..."
	docker compose up -d

docker-down:
	@echo "Stopping Docker Compose services..."
	docker compose down

docker-logs:
	@echo "Showing Docker Compose logs..."
	docker compose logs -f

docker-clean:
	@echo "Cleaning up Docker resources..."
	docker compose down -v --rmi all