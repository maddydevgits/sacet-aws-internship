# import the library
import paho.mqtt.client as mqtt

# create a client object 
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

# subscribe - receiver
client.subscribe('sacet/cse')

# define notification service
def notification(client,userdata,msg):
    print(msg.payload)

client.on_message=notification
client.loop_forever()
