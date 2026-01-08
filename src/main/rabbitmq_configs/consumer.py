import pika
from .callback import rabbitmq_callback
import os
from dotenv import load_dotenv
load_dotenv()

class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = os.getenv('RABBITMQ_HOST', 'localhost')
        self.__port = int(os.getenv('RABBITMQ_PORT', 5672))
        self.__username = os.getenv('RABBITMQ_USER', 'guest')
        self.__password = os.getenv('RABBITMQ_PASSWORD', 'guest')
        self.__queue = os.getenv('RABBITMQ_QUEUE', 'minha_queue')
        self.__channel = self.create_channel()

    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=rabbitmq_callback
        )
        return channel
    
    def start(self):
        self.__channel.start_consuming()

    