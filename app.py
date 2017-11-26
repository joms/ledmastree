#!flask/bin/python
import atexit
from flask import Flask, jsonify
from RPi import GPIO
from classes.controller import Controller as LEDController

APP = Flask(__name__)


CONTROLLER = LEDController()

@APP.route('/lampmastree/api/v1/leds', methods=['GET'])
def getLeds():
    return jsonify(CONTROLLER.getAll())

@APP.route('/lampmastree/api/v1/leds/<int:led_id>', methods=['GET'])
def getLet(led_id):
    return jsonify(CONTROLLER.get(led_id))

@APP.route('/lampmastree/api/v1/toggle', methods=['GET'])
def toggleLeds():
    return jsonify(CONTROLLER.toggleAll())

@APP.route('/lampmastree/api/v1/toggle/<int:led_id>', methods=['GET'])
def toggleLed(led_id):
    return jsonify(CONTROLLER.toggle(led_id))

@APP.route('/lampmastree/api/v1/on', methods=['GET'])
def onLeds():
    return jsonify(CONTROLLER.onAll())

@APP.route('/lampmastree/api/v1/on/<int:led_id>', methods=['GET'])
def onLed(led_id):
    return jsonify(CONTROLLER.on(led_id))

@APP.route('/lampmastree/api/v1/off', methods=['GET'])
def offLeds():
    return jsonify(CONTROLLER.offAll())

@APP.route('/lampmastree/api/v1/off/<int:led_id>', methods=['GET'])
def offLed(led_id):
    return jsonify(CONTROLLER.off(led_id))

if __name__ == '__main__':
    APP.run(debug=True)

def killswitch():
    GPIO.cleanup()

atexit.register(killswitch)
