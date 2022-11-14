import time

from stream_consumer.consumer import Consumer


def entry_point():

    while True:
        consumer = Consumer()
        response = consumer.return_stream_response()
        print(response)
        time.sleep(1)

if __name__ == "__main__":
    entry_point()