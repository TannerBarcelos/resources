package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"

	pb "github.com/tannerbarcelos/heartbeat/pb"
)

type server struct {
	pb.UnimplementedHealthServiceServer
}

func (s *server) GetHealth(ctx context.Context, req *pb.HealthRequest) (*pb.HealthResponse, error) {
	log.Println("GetHealth called")
	return &pb.HealthResponse{
		Status:  "UP",
		Version: "1.0.0",
	}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterHealthServiceServer(grpcServer, &server{})

	log.Println("HealthService server listening on :50051")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
