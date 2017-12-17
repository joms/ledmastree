"""Twitter stream handler"""
from time import sleep
import threading
from twython import TwythonStreamer

class Stream(TwythonStreamer):
    """Twitter stream class"""
    def __init__(self, flag, app_key, app_secret, oauth_token, oauth_token_secret, led_list, terms):
        self.led_list = led_list
        self.flag = flag
        self.brightness = 0

        thread = threading.Thread(target=self.tick)
        thread.start()

        TwythonStreamer.__init__(self, app_key, app_secret, oauth_token, oauth_token_secret)
        self.statuses.filter(track=terms)

    def tick(self):
        """Calculate DC based on time since last tweet (lolno)"""
        while not self.flag.isSet():
            if self.brightness > 0:
                self.brightness -= 5
            for key, item_ in self.led_list.items():
                if item_.pwm:
                    item_.pwm.ChangeDutyCycle(self.brightness)
            sleep(.01)
        
    def on_success(self, data):
        """success handler for twtter stream"""
        if 'text' in data and not self.flag.isSet():
            self.brightness = 100
