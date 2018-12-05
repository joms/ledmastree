"""Twitter support controller"""
import os
import threading
from .stream import Stream

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')

TERMS = '#Christmas'


class Twitter:
    """Twitter controller class"""
    def __init__(self, led_list):
        self.event_thread = False
        self.thread = False
        self.led_list = led_list

    def start_stream(self):
        """Start Twitter stream"""
        if self.event_thread:
            self.event_thread.clear()

        self.event_thread = threading.Event()
        self.thread = threading.Thread(target=Stream, args=(self.event_thread, APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, self.led_list, TERMS))
        self.thread.start()

    def stop_stream(self):
        """Stop Twitter stream"""
        if self.event_thread:
            self.event_thread.set()
