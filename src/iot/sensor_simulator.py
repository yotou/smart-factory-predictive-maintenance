import paho.mqtt.client as mqtt
import json
import random
import time

broker = "test.mosquitto.org"
topic = "factory/machine/sensor"

client = mqtt.Client()
client.connect(broker,1883)

while True:

    data = {
        "temperature": random.randint(60,100),
        "vibration": round(random.uniform(0.2,0.8),2),
        "pressure": random.randint(25,40),
        "humidity": random.randint(30,60)
    }

    client.publish(topic,json.dumps(data))

    print("sent:",data)

    time.sleep(5)