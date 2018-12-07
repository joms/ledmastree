"""Kafka consumer handler"""
from time import sleep
import threading
import json
import random
from kafka import KafkaConsumer

baselineBrightness = 5

class Listener:
    """Kafka consumer class"""

    def __init__(self, flag, kafka_hosts, kafka_topics, kafka_consumer_group, led_list):
        self.led_list = led_list
        self.flag = flag
        self.brightness = baselineBrightness

        thread = threading.Thread(target=self.tick)
        thread.start()

        self.consumer = KafkaConsumer(
            bootstrap_servers=kafka_hosts,  # '',
            group_id="Thor Heyerdal was here",
            enable_auto_commit=False,
            #auto_offset_reset='earliest'
        )

        self.consumer.subscribe(kafka_topics)
        for message in self.consumer:
            msgObj = json.loads(message.value.decode())

            if "method" in msgObj and msgObj["method"] == "ingested":
                for key, led in self.led_list.items():
                    led.set_brightness(100)
            else:
                for i in range(0, 5):
                    led = led_list[random.choice(list(self.led_list.keys())[1:])]
                    led.set_brightness(100)

    def tick(self):
        """Calculate DC based on time since last something (lolno)"""
        while not self.flag.isSet():
            for key, led in self.led_list.items():
                if led.pwm and key > 0 and led.brightness > baselineBrightness:
                    led.set_brightness(led.brightness - led.brightness/15)
            sleep(.02)

    def on_success(self, data):
        """success handler for kafka? stream"""
        print("success ran! what does this method do anyways?")
        if 'text' in data and not self.flag.isSet():
            self.brightness = 100
