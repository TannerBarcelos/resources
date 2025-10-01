NUM_ORDERS ?= 5

help:
	uv run main.py -h

run:
	uv run main.py --num-orders=$(NUM_ORDERS)

view-all-messages:
	docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning