# Learning gRPC: Multi-Language Distributed Systems

A hands-on learning project demonstrating gRPC communication between Node.js (TypeScript) and Go services, showcasing modern distributed systems patterns.

## 🎯 Learning Objectives

This repository demonstrates:
- **Cross-language gRPC communication** (Node.js ↔ Go)
- **Protocol Buffers** (protobuf) for service definitions
- **Docker containerization** for distributed deployment
- **Service-to-service communication** patterns
- **Health check implementations**
- **Environment-based configuration**

## 🏗️ Architecture

```
┌─────────────────┐    gRPC Call     ┌─────────────────┐
│   svc-1         │ ──────────────→  │   svc-2         │
│ (Node.js Client)│    Port 50051    │ (Go Server)     │
│                 │                  │                 │
│ - TypeScript    │                  │ - Go            │
│ - @grpc/grpc-js │                  │ - google.golang │
│ - Proto Loader  │                  │ - Generated PB  │
└─────────────────┘                  └─────────────────┘
         │                                    │
         └────────── Shared Proto ────────────┘
                   (health.proto)
```

## 📁 Project Structure

```
learning-grpc/
├── proto/                      # Shared Protocol Buffer definitions
│   └── health.proto           # Health service definition
├── svc-1/                     # Node.js gRPC Client
│   ├── index.ts              # TypeScript client implementation
│   ├── package.json          # Node.js dependencies
│   ├── tsconfig.json         # TypeScript configuration
│   └── Dockerfile            # Client container
├── svc-2/                     # Go gRPC Server  
│   ├── main.go               # Go server implementation
│   ├── go.mod                # Go module definition
│   ├── pb/                   # Generated Protocol Buffer files
│   │   ├── health.pb.go      # Generated message types
│   │   └── health_grpc.pb.go # Generated service interfaces
│   └── Dockerfile            # Server container
├── docker-compose.yml         # Multi-service orchestration
├── Makefile                  # Build automation
└── README.md                 # This documentation
```

## 🚀 Quick Start

### Prerequisites

- **Go** 1.19+
- **Node.js** 18+
- **pnpm** (or npm)
- **Docker** & **Docker Compose**
- **Protocol Buffers Compiler** (`protoc`)

### 1. Generate Protocol Buffer Code

```bash
# Generate Go code from proto files
make proto
```

### 2. Run with Docker (Recommended)

```bash
# Build and start both services
make docker-up

# View logs
make docker-logs

# Stop services
make docker-down
```

### 3. Run Locally

**Terminal 1 - Start Go Server:**
```bash
make run-server
# or manually:
cd svc-2 && go run main.go
```

**Terminal 2 - Run Node.js Client:**
```bash
make run-client
# or manually:
cd svc-1 && pnpm install && pnpm run dev
```

## 🔧 Development Workflow

### Protocol Buffer Development

1. **Edit** `proto/health.proto` to modify service definitions
2. **Generate** Go code: `make proto`
3. **Update** service implementations in `svc-2/main.go`
4. **Update** client calls in `svc-1/index.ts`

### Testing Changes

```bash
# Clean generated files
make clean

# Regenerate and test
make proto
make docker-up
```

## 📋 Available Commands

```bash
# Protocol Buffer generation
make proto              # Generate Go protobuf code
make clean              # Remove generated files

# Local development
make run-server         # Start Go gRPC server
make run-client         # Start Node.js client

# Docker operations
make docker-build       # Build all containers
make docker-up          # Start services with compose
make docker-down        # Stop and remove containers
make docker-logs        # View service logs

# Utilities
make help              # Show available commands
```

## 🌐 Service Details

### gRPC Server (svc-2) - Go

- **Port:** 50051
- **Language:** Go
- **Framework:** `google.golang.org/grpc`
- **Features:**
  - Health check endpoint
  - Structured logging
  - Docker containerization
  - Generated protobuf bindings

**Key Files:**
- `main.go` - Server implementation
- `pb/` - Generated protobuf code

### gRPC Client (svc-1) - Node.js

- **Language:** TypeScript/Node.js
- **Framework:** `@grpc/grpc-js`
- **Features:**
  - Dynamic proto loading
  - Environment-based server addressing
  - Error handling
  - Type-safe protobuf usage

**Key Files:**
- `index.ts` - Client implementation
- `package.json` - Dependencies

## 🔍 Learning Topics Covered

### 1. Protocol Buffers (protobuf)
- Service definition syntax
- Message types and fields
- Code generation for multiple languages

### 2. gRPC Communication Patterns
- Unary RPC calls
- Error handling
- Connection management
- Service discovery

### 3. Cross-Language Interoperability
- Go server ↔ Node.js client
- Shared protobuf definitions
- Type safety across languages

### 4. Containerization & Orchestration
- Multi-stage Docker builds
- Service dependencies
- Health checks
- Network isolation

### 5. Configuration Management
- Environment variables
- Service addressing
- Development vs production configs

## 🔄 Advanced Topics to Explore

### Server Reflection
Enable dynamic service discovery:

```go
// In svc-2/main.go
import "google.golang.org/grpc/reflection"

func main() {
    // ... existing code ...
    reflection.Register(grpcServer)
    // ... rest of code ...
}
```

### Streaming RPCs
Extend the proto definition:

```protobuf
service HealthService {
  rpc GetHealth (HealthRequest) returns (HealthResponse);
  rpc StreamHealth (HealthRequest) returns (stream HealthResponse);
}
```

### Interceptors/Middleware
Add logging, auth, or metrics:

```go
// Server interceptor example
grpcServer := grpc.NewServer(
    grpc.UnaryInterceptor(loggingInterceptor),
)
```

## 🐛 Troubleshooting

### Common Issues

1. **Proto generation fails:**
   ```bash
   # Ensure protoc is installed
   protoc --version
   
   # Install Go protobuf plugins
   go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
   go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
   ```

2. **Client connection refused:**
   ```bash
   # Check if server is running
   netstat -an | grep 50051
   
   # Verify Docker networks
   docker network ls
   ```

3. **Module resolution errors:**
   ```bash
   # In svc-2/ directory
   go mod tidy
   go mod download
   ```

## 📚 Additional Resources

- [gRPC Official Documentation](https://grpc.io/docs/)
- [Protocol Buffers Guide](https://developers.google.com/protocol-buffers)
- [Go gRPC Tutorial](https://grpc.io/docs/languages/go/quickstart/)
- [Node.js gRPC Guide](https://grpc.io/docs/languages/node/)

## 🤝 Contributing

Feel free to experiment and extend this learning project:

1. Add new RPC methods to the health service
2. Implement streaming RPCs
3. Add authentication/authorization
4. Implement client-side load balancing
5. Add monitoring and metrics

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning distributed systems concepts.
