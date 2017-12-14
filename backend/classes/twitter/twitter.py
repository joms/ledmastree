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
    def __init__(self, led_list):
        self.stream = Stream(led_list)

    def start_stream(self):
        self.stream.enabled = True
        
    def stop_stream(self):
        self.stream.enabled = False
    