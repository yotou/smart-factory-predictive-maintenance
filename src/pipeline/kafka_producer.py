from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:

    data = {
        "temperature": random.randint(60,100),
        "vibration": random.uniform(0.2,0.8),
        "pressure": random.randint(25,40),
        "humidity": random.randint(30,60)
    }

    producer.send("machine-sensor",data)

    print("sent to kafka",data)

    time.sleep(5)