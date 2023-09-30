import pika


def on_msg_recv(ch, method, properties, body):
    print(f"Consumer - Received A New Message! --> {body}")


conn_params = pika.URLParameters(
    "amqps://cpxigjdu:KwmgGn6w-V_6EQVWGtM2KELXm67nuCaV@octopus.rmq3.cloudamqp.com/cpxigjdu"
)
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()

channel.queue_declare(queue="consumer_queue")

channel.basic_consume(
    queue="consumer_queue",
    on_message_callback=on_msg_recv,
    auto_ack=True,
)

print("Consumer - Starting Consuming...")
channel.start_consuming()
channel.close()
