import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import * as path from 'path';

const PROTO_PATH = path.join(__dirname, 'proto/health.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: false,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;
const healthPackage = protoDescriptor.health;

// Use environment variable for server address, default to localhost for local development
const serverAddress = process.env.GRPC_SERVER_ADDRESS || 'localhost:50051';

const client = new healthPackage.HealthService(
    serverAddress,
    grpc.credentials.createInsecure()
);

client.GetHealth({}, (error: Error | null, response: any) => {
    if (error) {
        console.error('Error calling GetHealth:', error);
    } else {
        console.log('Health response:', response);
    }
});
