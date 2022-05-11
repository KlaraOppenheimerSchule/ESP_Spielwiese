import paho.mqtt.publish as publish
import time
from picamera import PiCamera
from time import sleep
from io import BytesIO
import broker.py

# setup server and topic
MQTT_SERVER = "Broker"
MQTT_PATH = "test_channel"

# Stopwatch: time to focus
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("%2d" %  (elapsed + 1))
        time.sleep(1)


camera = PiCamera()
camera.start_preview()

stopwatch(4)

broker = Broker('guenter')

buff=BytesIO()

camera.capture(buff, format = 'jpeg')
print("capture...")

buff.seek(0)
broker.send_file(MQTT_PATH, buff.read())
print("send...")

camera.stop_preview()
print("DONE")
