from confluent_kafka import Producer
import os

producer = Producer({
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'LVYMA3GZ2TYB6P3M',
    'sasl.password': '0Sr17E4dVe6DcRYoZB9cMsUafmec4mru3s21UnD7eK6s04CoGMW/PxQgyvVCtOTY',
    'sasl.mechanism': 'PLAIN',
})
