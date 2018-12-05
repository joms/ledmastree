"""Twitter stream handler"""
from time import sleep
import threading
from kafka import KafkaConsumer


class Listener(KafkaConsumer):
    """Twitter stream class"""

    def __init__(self, flag, kafka_hosts, kafka_topics, kafka_consumer_group, led_list):
        self.led_list = led_list
        self.flag = flag
        self.brightness = 0

        thread = threading.Thread(target=self.tick)
        thread.start()

        self.consumer = KafkaConsumer(
            bootstrap_servers=kafka_hosts,  # '',
            group_id=kafka_consumer_group,
            enable_auto_commit=False,
            #               auto_offset_reset='earliest'
        )

        self.consumer.subscribe(kafka_topics)

    def tick(self):
        """Calculate DC based on time since last something (lolno)"""
        while not self.flag.isSet():
            if self.brightness > 0:
                self.brightness -= 5
            for key, item_ in self.led_list.items():
                if item_.pwm:
                    item_.pwm.ChangeDutyCycle(self.brightness)
            sleep(.02)

    def on_success(self, data):
        """success handler for twtter stream"""
        if 'text' in data and not self.flag.isSet():
            self.brightness = 100
