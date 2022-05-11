import base64
import time
import broker.py

# setup counter for images
anzahl = open("number.txt").read()
type(anzahl)
nummer=int(anzahl)
nummer=nummer+1
benennung= str(nummer)

file=open("number.txt","w")
file.write(benennung)
file.close()



# setup decoding and writing image
def callback(cid, userdata, msg, ):
    print('received something')
    ##print(str(msg.payload))
    try:
        with open('/media/extern/Images/image' + benennung + 'jpeg', 'wb') as out:
        #with open('test.jpeg', 'wb') as out:

            temp = str(msg.payload)[2:-1]
            ##print("Image saved "+str(len(temp)))
            temp2 = base64.b64decode(temp)
            out.write(temp2)
            print("Image saved")
            
    except Exception as e:
        print("fail")
        print(e)

subs = {
    'test_channel': callback
}

# hostname: hostname of publishing client
b = Broker('jockel', host='gruppe11', subscriptions=subs)

while True:
    time.sleep(1)
