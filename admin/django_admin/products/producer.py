import pika

# from pika.exchange_type import ExchangeType

conn_params = pika.URLParameters(
    "amqps://cpxigjdu:KwmgGn6w-V_6EQVWGtM2KELXm67nuCaV@octopus.rmq3.cloudamqp.com/cpxigjdu"
)
conn = pika.BlockingConnection(conn_params)
channel = conn.channel()


channel.queue_declare(queue="consumer_queue")

MSG: str = "working right!"


def publish():
    channel.basic_publish(
        exchange="",
        routing_key="consumer_queue",
        body=MSG,
    )

    print(f"Sent message: {MSG}")


# publish()

# conn.close()
