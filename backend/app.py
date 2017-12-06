#!flask/bin/python
""" API router for our xmas tree"""
import atexit
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from RPi import GPIO
from classes.controller import Controller as LEDController

APP = Flask(__name__)
CORS(APP, support_credentials=True)


CONTROLLER = LEDController()

@APP.route('/ledmastree/api/v1/leds', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_leds():
    """Get all LEDs"""
    return jsonify(CONTROLLER.get_all())

@APP.route('/ledmastree/api/v1/leds/<int:led_id>', methods=['GET'])
def get_led(led_id):
    """Get a single LED"""
    return jsonify(CONTROLLER.get(led_id))

@APP.route('/ledmastree/api/v1/toggle', methods=['GET'])
def toggle_leds():
    """Toggle all LEDs"""
    return jsonify(CONTROLLER.toggle_all())

@APP.route('/ledmastree/api/v1/toggle/<int:led_id>', methods=['GET'])
def toggle_led(led_id):
    """Toggle single LED"""
    return jsonify(CONTROLLER.toggle(led_id))

@APP.route('/ledmastree/api/v1/on', methods=['GET'])
def on_leds():
    """Turn all LEDs on"""
    return jsonify(CONTROLLER.on_all())

@APP.route('/ledmastree/api/v1/on/<int:led_id>', methods=['GET'])
def on_led(led_id):
    """Turn a single LED on"""
    return jsonify(CONTROLLER.on(led_id))

@APP.route('/ledmastree/api/v1/off', methods=['GET'])
def off_leds():
    """Turn all LEDs off"""
    return jsonify(CONTROLLER.off_all())

@APP.route('/ledmastree/api/v1/off/<int:led_id>', methods=['GET'])
def off_led(led_id):
    """Turn a single LED off"""
    return jsonify(CONTROLLER.off(led_id))

@APP.route('/ledmastree/api/v1/pwm/<string:state>', methods=['GET'])
def set_pwm_leds(state):
    """Set PWM on all LEDs"""
    return jsonify(CONTROLLER.set_pwm_leds(state))

@APP.route('/ledmastree/api/v1/patterns', methods=['GET'])
def get_patterns():
    """Get all patterns"""
    return jsonify(CONTROLLER.get_patterns())

@APP.route('/ledmastree/api/v1/patterns/<int:pattern_id>/<string:command>', methods=['GET'])
def set_pattern(pattern_id, command):
    """Activate or deactivate a pattern"""
    return jsonify(CONTROLLER.set_pattern(pattern_id, command))

if __name__ == '__main__':
    APP.run(debug=True)

def killswitch():
    """Clean up GPIO pins on death"""
    GPIO.cleanup()

atexit.register(killswitch)
