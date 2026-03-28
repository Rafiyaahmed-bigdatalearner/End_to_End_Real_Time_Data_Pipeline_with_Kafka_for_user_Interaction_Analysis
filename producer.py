# producer.py
from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Types of user interactions
INTERACTION_TYPES = ["click", "view", "purchase"]

# Connect to Kafka running inside Docker on Windows
producer = KafkaProducer(
    bootstrap_servers='host.docker.internal:9092',  # Windows + Docker fix
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    return {
        "user_id": f"user_{random.randint(1, 100)}",
        "item_id": f"item_{random.randint(1, 50)}",
        "interaction_type": random.choice(INTERACTION_TYPES),
        "timestamp": datetime.utcnow().isoformat()
    }

# Number of events per second
RATE_PER_SEC = 10  # Start smaller for testing

print("Producer started... sending events to Kafka")

while True:
    for _ in range(RATE_PER_SEC):
        event = generate_event()
        producer.send("user_interactions", value=event)
        print("Sent:", event)
    producer.flush()  # Ensure messages are sent
    time.sleep(1)