import json
import pika
from celery import current_task, shared_task
from rab_test_cel.online_account.models import OnlineAccount

@shared_task
def listen_to_rabbitmq():
    credentials = pika.credentials.PlainCredentials(username="guest", password="guest")
    # RabbitMQ connection parameters
    parameters = pika.ConnectionParameters(
        host="rabbitmq", port=5672, virtual_host="/", credentials=credentials
    )
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue="datum_taml_broker")

    def callback(ch, method, properties, body):
        # Execute the Celery task when a message is received
        print("[W] Waiting for message")
        body = json.loads(body)
        print(f"[GM] { body }")
        OnlineAccount.objects.create(task_id=current_task.request.id, account_detail=body)

    channel.basic_consume(
        queue="datum_taml_broker", on_message_callback=callback, auto_ack=True
    )

    # Start the RabbitMQ consumer
    print("[W] Waiting for start consuming")
    try:
        # Start consuming messages from the queue
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupt")
        channel.stop_consuming()
    finally:
        print("closed")
        connection.close()
