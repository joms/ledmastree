"""Kafka support controller"""
import os
import threading
from .listener import Listener

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

KAFKA_HOSTS = os.environ.get('KAFKA_HOSTS_CSV', '').split(';')
KAFKA_TOPICS = os.environ.get('KAFKA_TOPICS', '').split(';')
KAFKA_CONSUMER_GROUP = os.environ.get('KAFKA_CONSUMER_GROUP')


class Kafka:
    """Kafka controller class"""
    def __init__(self, led_list):
        self.event_thread = False
        self.thread = False
        self.led_list = led_list

    def start_kafka(self):
        """Start kafka listener"""
        if self.event_thread:
            self.event_thread.clear()

        self.event_thread = threading.event()
        self.thread = threading.Thread(target=Listener, args=(self.event_thread, KAFKA_HOSTS, KAFKA_TOPICS, KAFKA_CONSUMER_GROUP, self.led_list))


    def stop_kafka(self):
        """Stop kafka listener"""
        if self.event_thread:
            self.event_thread.set()
