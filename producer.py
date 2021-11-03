import json
import random
from kafka import KafkaProducer
from data_geneator import generate_message
import time

def serializer(meessage):
    return json.dumps(meessage).encode('utf-8')


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':

    while True:
        dummy_messages = generate_message()
        producer.send('messages2', dummy_messages)

        time.sleep(random.randint(1,5))