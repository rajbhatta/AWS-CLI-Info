import calendar
import random
import time
from datetime import datetime

from stream_producer.kinesisutil import KinesisUtil


def entry_point():
    kinesis_utl = KinesisUtil()
    while True:
        property_value = random.randint(40, 120)
        property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
        thing_id = 'Sensor-0x1234f'

        kinesis_utl.send_data_to_stream(thing_id, property_value, property_timestamp)

        # wait for 5 second
        time.sleep(5)


if __name__ == "__main__":
    entry_point()