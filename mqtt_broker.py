#!/usr/bin/pythob
# -*- coding: utf-8 -*-

# pub msg: mosquitto_pub -d -t /sensor/Topic -m "message"

import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
	msg = str(message.payload.decode("utf-8"))
	print("message revceived: " , msg)
	print("message topic: ", message.topic)
		
		
def on_connect(client, userdata, flags, rc):
	client.subscribe('/sensor')	
	client.subscribe('/sensor/co2Level')
	client.subscribe('/sensor/airTemp')
	client.subscribe('/sensor/Humidity')
	client.subscribe('/sensor/personCounter')
	client.subscribe('/sensor/windowState')

BROCKER_ADDRESS = "192.168.102.191"
# 192.168.102.191
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROCKER_ADDRESS)

print("Connected to MQTT_Brocker: " + BROCKER_ADDRESS)

client.loop_forever()
