from confluent_kafka import Producer
from utility import functions

class KafkaConnector():
    
    def set_producer(self):
        return Producer({'bootstrap.servers': functions.get_kafka_cnn_str(self.bootstrap_servers, self.bootstrap_port)})
    
    def __init__(self, bootstrap_servers='localhost', bootstrap_port='9092'):
        self.bootstrap_servers = bootstrap_servers
        self.bootstrap_port = bootstrap_port
        self.producer = self.set_producer()

    def produce(self, topic, msg_key, message):
        self.producer.produce(topic, key=msg_key, value=message)
        print("msg sent: " + msg_key)

    def flush_producer(self):
        print("flushing the producer")
        self.producer.flush(30)