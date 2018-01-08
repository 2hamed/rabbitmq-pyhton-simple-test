import pika
import sys


def callback(ch, method, properties, body):
    print("Message: %s" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

sendUser = sys.argv[1]

channel.queue_declare(queue=sendUser)
channel.basic_consume(callback, queue=sendUser, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()