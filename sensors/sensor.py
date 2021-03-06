import time
import json
import redis
from nanpy import (ArduinoApi, SerialManager)

default_connection = SerialManager()

class Sensor():

	def __init__(self, pin, name='Sensor', connection=default_connection, analog_pin_mode=False, key=None):
		self.pin = pin
		self.name = name
		self.key = key.replace(" ", "_").lower() if key is not None else self.name.replace(" ", "_").lower()
		self.analog_pin_mode = analog_pin_mode
		self.connection = connection
		self.api = ArduinoApi(connection)
		return

	def init_sensor(self):
		#Initialize the sensor here (i.e. set pin mode, get addresses, etc)
		pass

	def read(self):
		#Read the sensor(s), parse the data and store it in redis if redis is configured
		pass

	def readRaw(self):
		#Read the sensor(s) but return the raw data, useful for debugging
		pass

	def readPin(self):
		#Read the pin from the ardiuno. Can be analog or digital based on "analog_pin_mode"
		data = self.api.analogRead(self.pin) if analog_pin_mode else self.api.digitalRead(self.pin)
		return data