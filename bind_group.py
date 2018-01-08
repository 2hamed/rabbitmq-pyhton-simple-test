import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
op = sys.argv[1]
sendUser = sys.argv[2]
group = sys.argv[3]

channel.queue_declare(queue=sendUser)
channel.exchange_declare(exchange=group, exchange_type='fanout')

if op == 'bind':
    channel.queue_bind(queue=sendUser, exchange=group)
else:
    channel.queue_unbind(queue=sendUser, exchange=group)
