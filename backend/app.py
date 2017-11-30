#!flask/bin/python
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

@APP.route('/ledmastree/api/v1/pwm/<string:state>', methods=['GET'])
def set_pwm_leds(state):
    return jsonify(CONTROLLER.pwm_all(state))

@APP.route('/ledmastree/api/v1/pwm/<string:state>/<int:led_id>', methods=['GET'])
def set_pwm_leds(state, led_id):
    return jsonify(CONTROLLER.pwm(state, led_id))

if __name__ == '__main__':
    APP.run(debug=True)

def killswitch():
    GPIO.cleanup()

atexit.register(killswitch)
