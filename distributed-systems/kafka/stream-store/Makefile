NUM_ORDERS ?= 5

help:
	uv run producer.py -h

run-producer:
	uv run producer.py --num-orders=$(NUM_ORDERS)
run-consumer:
	uv run consumer.py

view-all-messages:
	docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning