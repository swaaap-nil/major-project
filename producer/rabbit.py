import traceback
import pika
import json

class RabbitMQHelper:
    def __init__(self, host='localhost', user='user@notification', password='password@notification', port=5672):
        self.host = host
        self.port = port
        self.credentials = pika.PlainCredentials(user,password)
        self.connection_params = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=self.credentials
        )

    def publish_message(self, queue: str, message: dict):
        """Publish a message to the RabbitMQ queue."""
        try:
            connection = pika.BlockingConnection(self.connection_params)
            channel = connection.channel()

            # Declare queue (ensures it exists)
            channel.queue_declare(queue=queue, durable=True)

            # Convert message to JSON and publish
            channel.basic_publish(
                exchange='',
                routing_key=queue,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2  # Make message persistent
                )
            )

            print(f"[✔] Sent to '{queue}': {message}")

            connection.close()

        except Exception as e:
            print("[❌] Error publishing message:", e)

    def consume_messages(self, queue: str, callback_function):
        """Consume messages from RabbitMQ queue and process with callback."""
        try:
            connection = pika.BlockingConnection(self.connection_params)
            channel = connection.channel()

            # Declare queue (ensures it exists)
            channel.queue_declare(queue=queue, durable=True)

            def callback(ch, method, properties, body):
                message = json.loads(body)
                print(f"[📩] Received from '{queue}': {message}")

                # Call user-provided function to process the message
                callback_function(message)

                ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge message

            channel.basic_consume(queue=queue, on_message_callback=callback)

            print(f"[*] Waiting for messages from '{queue}'... Press CTRL+C to exit.")
            channel.start_consuming()

        except Exception as e:
            print("[❌] Error consuming messages:", e)
            traceback.print_exc()
