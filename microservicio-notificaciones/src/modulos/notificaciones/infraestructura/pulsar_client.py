import pulsar

class PulsarClient:
    def __init__(self, service_url='pulsar://localhost:6650'):
        self.client = pulsar.Client(service_url)
    
    def create_consumer(self, topic, subscription_name):
        return self.client.subscribe(topic, subscription_name)
    
    def close(self):
        self.client.close()
