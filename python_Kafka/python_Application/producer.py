import json
import requests
#from kafka import KafkaProducer
from confluent_kafka import Producer
from time import sleep

# producer = KafkaProducer(
#     bootstrap_servers='localhost:9094',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

conf = {'bootstrap.servers': 'localhost:9094'}
producer = Producer(conf)

def fetch_joke():
    url = 'https://v2.jokeapi.dev/joke/Programming?type=single'
    response = requests.get(url)
    data = response.json()
    return data

def produce_data():
    while True:
        joke = fetch_joke()
        producer.produce('test-topic', key='key', value=json.dumps(joke))
        print(f"Sent: {joke}")
        producer.flush()
        sleep(5)
        

if __name__ == "__main__":
    produce_data()
