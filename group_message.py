import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

group = sys.argv[1]
message = sys.argv[2]

channel.basic_publish(exchange=group,
                      routing_key='',
                      body=message)

connection.close()
