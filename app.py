#!flask/bin/python
import atexit
from flask import Flask, jsonify
from RPi import GPIO
from classes.controller import Controller as LEDController

APP = Flask(__name__)


CONTROLLER = LEDController()

@APP.route('/ledmastree/api/v1/leds', methods=['GET'])
def get_leds():
    return jsonify(CONTROLLER.get_all())

@APP.route('/ledmastree/api/v1/leds/<int:led_id>', methods=['GET'])
def get_led(led_id):
    return jsonify(CONTROLLER.get(led_id))

@APP.route('/ledmastree/api/v1/toggle', methods=['GET'])
def toggle_leds():
    return jsonify(CONTROLLER.toggle_all())

@APP.route('/ledmastree/api/v1/toggle/<int:led_id>', methods=['GET'])
def toggle_led(led_id):
    return jsonify(CONTROLLER.toggle(led_id))

@APP.route('/ledmastree/api/v1/on', methods=['GET'])
def on_leds():
    return jsonify(CONTROLLER.on_all())

@APP.route('/ledmastree/api/v1/on/<int:led_id>', methods=['GET'])
def on_led(led_id):
    return jsonify(CONTROLLER.on(led_id))

@APP.route('/ledmastree/api/v1/off', methods=['GET'])
def off_leds():
    return jsonify(CONTROLLER.off_all())

@APP.route('/ledmastree/api/v1/off/<int:led_id>', methods=['GET'])
def off_led(led_id):
    return jsonify(CONTROLLER.off(led_id))

if __name__ == '__main__':
    APP.run(debug=True)

def killswitch():
    GPIO.cleanup()

atexit.register(killswitch)
