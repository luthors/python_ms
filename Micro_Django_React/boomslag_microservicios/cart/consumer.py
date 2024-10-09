import json, os, django
from confluent_kafka import Consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.apps import apps

Cart = apps.get_model('cart', 'Cart')

# Endpoints
# 'Bootstrap server': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092'
# 'security protocol': 'SASL_SSL'
# 'sasl username': 'LVYMA3GZ2TYB6P3M'
# 'sasl password': '0Sr17E4dVe6DcRYoZB9cMsUafmec4mru3s21UnD7eK6s04CoGMW/PxQgyvVCtOTY'
# 'sasl mechanism': 'PLAIN'
# 'group id': 'cart_group'
# 'auto.offset.reset': 'earliest'

consumer = Consumer({
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'LVYMA3GZ2TYB6P3M',
    'sasl.password': '0Sr17E4dVe6DcRYoZB9cMsUafmec4mru3s21UnD7eK6s04CoGMW/PxQgyvVCtOTY',
    'sasl.mechanism': 'PLAIN',
    'group.id': 'aaa',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['user_register'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    print('Received message with Value: {}'.format(msg.value()))
    print('Message Topic: {}'.format(msg.topic()))
    print('Message Key: {}'.format(msg.key()))
    
    topic = msg.topic()
    value = msg.value()
    
    if topic == 'user_register':
        
        print('topic: {}'.format(topic))
        print('value: {}'.format(value))
        
        
        if msg.key() == b'create_user':
            print('Creating cart for user: {}'.format(value))
            user_data = json.loads(value)
            user_id = user_data['id']
            cart, created = Cart.objects.get_or_create(user_id=user_id, defaults={'total_items': 0})
            if created:
                print('Cart created for user: {}'.format(user_id))
                cart.save()
        pass

consumer.close()