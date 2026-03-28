# aggregator.py
from kafka import KafkaConsumer
import json
from collections import defaultdict
import threading
import time

# Aggregation dictionaries
user_counts = defaultdict(int)
item_counts = defaultdict(int)

# Alert threshold
THRESHOLD = 100

# Kafka consumer
consumer = KafkaConsumer(
    'user_interactions',
    bootstrap_servers='host.docker.internal:9092',  # Windows + Docker fix
    auto_offset_reset='earliest',  # Read from start if no offset
    enable_auto_commit=True,
    group_id='aggregator-group',   # Unique consumer group
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Consume messages
def consume():
    for message in consumer:
        event = message.value
        user_counts[event['user_id']] += 1
        item_counts[event['item_id']] += 1

# Save aggregated data to JSON for dashboard
def save_to_json():
    while True:
        data = {"users": dict(user_counts), "items": dict(item_counts)}
        with open("aggregated_data.json", "w") as f:
            json.dump(data, f, indent=2)
        time.sleep(2)

# Print alerts when threshold exceeded
def check_alerts():
    while True:
        for item, count in item_counts.items():
            if count > THRESHOLD:
                print(f"ALERT: {item} exceeded {THRESHOLD}")
        time.sleep(3)

# Start threads
threading.Thread(target=consume, daemon=True).start()
threading.Thread(target=save_to_json, daemon=True).start()
threading.Thread(target=check_alerts, daemon=True).start()

print("Aggregator started... listening to Kafka")

# Keep main thread alive
while True:
    time.sleep(1)