import json
import time
from kafka import KafkaConsumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'kpi_sink'
consumer = KafkaConsumer(TOPIC, bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_deserializer=lambda x: json.loads(x), auto_offset_reset='earliest')
for msg in consumer:
    print(msg.key, msg.value)
