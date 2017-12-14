import os
import threading
from twython import TwythonStreamer

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')

TERMS = '#Christmas'

class Twitter:
    def __init__(self, led_list):
        self.led_list = led_list

        self.event_thread = False
        self.thread = False

        self.stream = TwythonStreamer.__init__(self, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.stream.statuses.filter(track=TERMS)

    def start_stream(self):
        self.event_thread = threading.Event()
        self.thread = threading.Thread(name='non-block', target=func, args=(self.event_thread, .1))
        self.thread.start()
        
    def stop_stream(self):
        if self.event_thread:
            self.event_thread.set()
            self.event_thread = False
            self.thread = False
    