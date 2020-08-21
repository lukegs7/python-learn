import json
import time
from kafka import KafkaProducer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'kpi_source'
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS, key_serializer=lambda x: x.encode('utf-8'),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for x in range(10):
    kpi_key = f'kpi.dashboard1.{x}'
    producer.send(TOPIC, key=kpi_key,
                  value={'kpi_key': kpi_key, 'timestamp': int(time.time()) * 1000, 'value': 1.12312})
producer.flush()
producer.close()
