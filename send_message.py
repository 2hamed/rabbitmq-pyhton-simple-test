import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

sendUser = sys.argv[1]
message = sys.argv[2]

channel.queue_declare(queue=sendUser)

channel.basic_publish(exchange='',
                      routing_key=sendUser,
                      body=message)

connection.close()
