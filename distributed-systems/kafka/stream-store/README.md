# Kafka Stream Store

A Python-based Kafka streaming application that demonstrates event streaming with order processing. This project showcases producer-consumer patterns using Apache Kafka for real-time data streaming.

## 🚀 Features

- **Order Producer**: Generates and publishes fake order events to Kafka topics
- **Order Consumer**: Subscribes to order topics and processes incoming events
- **Event Tracking**: Comprehensive audit logging for all order events
- **Docker Integration**: Containerized Kafka setup with KRaft mode (no ZooKeeper required)
- **Configuration Management**: YAML-based configuration for different environments
- **CLI Interface**: Command-line tools for easy producer and consumer management

## 📋 Prerequisites

- Python 3.13+
- Docker and Docker Compose
- [UV](https://docs.astral.sh/uv/) package manager

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd stream-store
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Start Kafka infrastructure**
   ```bash
   docker-compose up -d
   ```

## 🎯 Quick Start

### Start the Order Consumer (Event Tracker)
```bash
# Using UV
uv run consumer.py

# Using Makefile
make run-consumer
```

### Generate and Send Orders
```bash
# Send 5 orders (default)
uv run producer.py

# Send custom number of orders
uv run producer.py --num-orders=10

# Using Makefile
make run-producer NUM_ORDERS=20
```

### View All Messages in Kafka
```bash
make view-all-messages
```

## 📁 Project Structure

```
stream-store/
├── producer.py          # Kafka producer for generating order events
├── consumer.py          # Kafka consumer for processing order events
├── docker-compose.yaml  # Kafka infrastructure setup
├── Makefile            # Development commands
├── pyproject.toml      # Project dependencies and metadata
├── uv.lock            # Dependency lock file
├── config/
│   └── dev.yaml       # Development configuration
└── lib/
    ├── cli.py         # Command-line argument parsing
    ├── config.py      # Configuration management
    ├── logger.py      # Logging utilities
    ├── orders.py      # Order data generation
    └── util.py        # Common utilities
```

## ⚙️ Configuration

The application uses YAML configuration files located in the `config/` directory. Key configuration options:

```yaml
kafka:
  bootstrap_servers: "localhost:9092"
  topics:
    orders: "orders"
  consumer:
    group_id: "order-tracker"
    auto_offset_reset: "earliest"
    poll_timeout: 1.0
  producer:
    delivery_timeout: 30

application:
  default_num_orders: 5
  log_level: "INFO"
```

## 🔧 Development Commands

| Command | Description |
|---------|-------------|
| `make help` | Show producer help |
| `make run-producer` | Run order producer with default settings |
| `make run-consumer` | Start order consumer/tracker |
| `make view-all-messages` | View all messages in Kafka topic |

## 📊 Architecture

### Producer Flow
1. Generates fake order data using Faker library
2. Serializes orders to JSON format
3. Publishes messages to Kafka `orders` topic
4. Provides delivery confirmation callbacks

### Consumer Flow
1. Subscribes to `orders` topic
2. Continuously polls for new messages
3. Processes and logs received orders
4. Acts as an audit trail for all order events

### Data Model
Each order event contains:
- `order_id`: Unique order identifier
- `item_id`: Unique item identifier
- `item`: Item name
- `quantity`: Number of items ordered
- `user`: Username of the customer

## 🐳 Docker Services

The project includes a complete Kafka setup using Docker:

- **Kafka Broker**: Runs in KRaft mode (no ZooKeeper dependency)
- **Port**: 9092 (exposed to localhost)
- **Data Persistence**: Kafka data is persisted in Docker volumes

## 🧪 Testing

Generate test orders and verify the complete pipeline:

1. Start the consumer in one terminal
2. Run the producer in another terminal
3. Observe real-time order processing in the consumer logs
4. Use `make view-all-messages` to inspect all messages in Kafka

## 🔍 Monitoring

The application provides detailed logging for:
- Producer message delivery status
- Consumer message processing
- Kafka connection status
- Error handling and recovery

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of a distributed systems learning resource.

## 🆘 Troubleshooting

### Common Issues

**Kafka Connection Failed**
- Ensure Docker containers are running: `docker-compose ps`
- Check if port 9092 is available
- Verify Kafka logs: `docker-compose logs kafka`

**Consumer Not Receiving Messages**
- Verify topic exists and has messages
- Check consumer group configuration
- Ensure producer has successfully sent messages

**Permission Errors**
- Check Docker daemon is running
- Verify user permissions for Docker commands

---

Built with ❤️ for learning distributed systems and event streaming patterns.