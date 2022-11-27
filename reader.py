import os
import sys
from time import sleep

import pika
import psycopg2
from psycopg2 import sql

host = os.environ['HOST']
port = os.environ['PORT']
username = os.environ['LOGIN']
password = os.environ['PASSWORD']
postgres_db = os.environ['POSTGRES_DB']
postgres_user = os.environ['POSTGRES_USER']
postgres_password = os.environ['POSTGRES_PASSWORD']
postgres_host = os.environ['POSTGRES_HOST']

# host = 'localhost'
# port = 5672
# username = 'bobra'
# password = '2a55f70a841f18b97c3a7db939b7adc9e34a0f1b'


def get_cursor():
    conn = psycopg2.connect(dbname=postgres_db, user=postgres_user,
                            password=postgres_password, host=postgres_host)
    cursor = conn.cursor()
    print('Connected to postgres', flush=True)
    return conn, cursor


def callback(ch, method, properties, body):
    log_message_to_postgres(body.decode())
    print(" [x] Received %r" % body, flush=True)


def log_message_to_postgres(message):
    conn, cursor = get_cursor()
    if 'bebra' in message:
        table = 'messages1'
    else:
        table = 'messages2'
    conn.autocommit = True
    cursor.execute(f"INSERT INTO {table} (message_text) VALUES (%s)", (message,))
    cursor.close()
    conn.close()
    print('Closed connection to postgres', flush=True)


def main():
    print(f'Connecting to {host}:{port} with username {username}', flush=True)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host, port=port, credentials=pika.PlainCredentials(username, password)))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages', flush=True)
    channel.start_consuming()


if __name__ == '__main__':
    print('Starting in 10 seconds', flush=True)
    sleep(1)
    print('Starting now', flush=True)
    main()
