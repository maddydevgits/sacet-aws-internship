# it has to publish a message - sending
# pip install paho-mqtt 

import paho.mqtt.client as mqtt
import time

# client - class , object - class members
client=mqtt.Client()

while True:
    # connect with broker
    client.connect('broker.hivemq.com',1883)
    print('Broker Connected')

    # publishing the message
    client.publish('sacet/cse','internship is going well')
    time.sleep(4)
