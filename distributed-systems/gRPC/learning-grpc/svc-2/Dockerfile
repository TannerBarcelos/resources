FROM golang:1.23-alpine AS builder

WORKDIR /app

# Copy go mod files
COPY svc-2/go.mod svc-2/go.sum ./

# Download dependencies
RUN go mod download

# Copy source code
COPY svc-2/ .

# Build the application
RUN go build -o main .

# Final stage
FROM alpine:latest

# Install netcat for health check
RUN apk add --no-cache netcat-openbsd

WORKDIR /app

# Copy the binary from builder
COPY --from=builder /app/main .

# Expose the port
EXPOSE 50051

# Run the application
CMD ["./main"]
