from twython import TwythonStreamer

class Stream(TwythonStreamer):
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret, led_list):
        self.led_list = led_list
        self.enabled = False
        TwythonStreamer.__init__(self, app_key, app_secret, oauth_token, oauth_token_secret)

    def on_success(self, data):
        if 'text' in data && self.enabled:
            print(data['text'].encode('utf-8'))
            print("\n")    
        #self.lightControl.bumpPower()
