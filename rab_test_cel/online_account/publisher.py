import json
try:
    import pika
except Exception as e:
    print(f"Import issues { e }")

credentials = pika.credentials.PlainCredentials(
        username="guest",
        password="guest"
    )


class RabbitMQServer:
    def __init__(self, queue='datum_taml_broker'):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="rabbitmq",
                port=5672,
                virtual_host="/",
                credentials=credentials,
            )
        )
        self.channel = self.connection.channel()
        self.queue = queue
        self.channel.queue_declare(queue=self.queue)

    def publish(self, payload={}):
        bbb = json.dumps(payload)
        self.channel.basic_publish(exchange="", routing_key="datum_taml_broker", body=bbb)
        print("Message Published !!!")
        self.connection.close()


# if __name__ == "__main__":
#     server = RabbitMQ(queue="datum_taml_broker")
#     server.publish(payload={"data":"hello test message", "data_2": "hello test 2 data"})