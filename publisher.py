import pika
import json
import os
from dotenv import load_dotenv
load_dotenv()

class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = os.getenv('RABBITMQ_HOST', 'localhost')
        self.__port = int(os.getenv('RABBITMQ_PORT', 5672))
        self.__username = os.getenv('RABBITMQ_USER', 'guest')
        self.__password = os.getenv('RABBITMQ_PASSWORD', 'guest')
        self.__exchange = os.getenv('RABBITMQ_EXCHANGE', 'minha_exchange')
        self.__routing_key = ""
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
        
        return channel

    def send_message(self, body:dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2  
            )
        )

rabbit_mq_publisher = RabbitMQPublisher()
rabbit_mq_publisher.send_message({
    "message": "Finalizado!!!"
})


