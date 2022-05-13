import base64
import time
import broker.py


# setup decoding and writing image
def callback(cid, userdata, msg, ):
    print('received something')
    ##print(str(msg.payload))
    try:
        print(str(msg.payload))
            
    except Exception as e:
        print("fail")
        print(e)

subs = {
    'test_channel': callback
}

# hostname: hostname of publishing client
b = Broker('jockel', host='PiBrocker', subscriptions=subs)

while True:
    time.sleep(1)
