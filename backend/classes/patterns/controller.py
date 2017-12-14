"""LED pattern controller"""
import threading
import time
from .patterns import Patterns

class Controller:
    """Led pattern controller class"""
    def __init__(self, led_list):
        self.patterns = Patterns(led_list)

        self.active_pattern = False
        self.event_thread = False
        self.thread = False

    def start(self, id_):
        """Start a pattern"""
        pattern = self.patterns.get_pattern(id_)
        func = getattr(self.patterns, pattern["trigger"])

        if self.event_thread:
            self.stop()

        self.event_thread = threading.Event()
        self.thread = threading.Thread(name='non-block', target=func, args=(self.event_thread, .1))
        self.thread.start()

        self.active_pattern = pattern
        return self.active_pattern

    def stop(self):
        """Stop a pattern"""
        if self.event_thread:
            self.event_thread.set()
            self.event_thread = False
            self.thread = False
