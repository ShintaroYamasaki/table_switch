from flask import Flask, jsonify, abort, make_response

#from grovepi import *

import wiringpi

pin_num = 24
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pin_num, wiringpi.INPUT)

api = Flask(__name__)


@api.route('/', methods=['GET'])
def get():
  value = wiringpi.digitalRead(pin_num)
  result = {
    "value": value
  }

  return jsonify(value=value)

@api.errorhandler(404)
def not_found(error):
  return jsonify(error='Not found')

if __name__ == '__main__':
  api.run(host='0.0.0.0', port=3000)
