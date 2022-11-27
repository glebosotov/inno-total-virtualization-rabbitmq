import os
from time import sleep, time

import pika

host = os.environ['HOST']
port = os.environ['PORT']
username = os.environ['LOGIN']
password = os.environ['PASSWORD']

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host, port=port, credentials=pika.PlainCredentials(username, password)))
channel = connection.channel()

channel.queue_declare(queue='hello')
counter = 0
try:
    while (True):
        sleep(1)
        counter = counter + 1
        message = 'bebra' if counter % 2 == 0 else 'bobra'
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print(" [x] Sent a message", flush=True)
except KeyboardInterrupt:
    connection.close()