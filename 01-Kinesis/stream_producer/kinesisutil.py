import json

import boto3 as boto3
import kinesis as kinesis
import sys

from random import seed
from random import randint
import time
import random

class KinesisUtil():

    def __init__(self):
        self.__kinesis_client = boto3.client('kinesis', region_name='us-west-2')

    def send_data_to_stream(self,thing_id, property_value, property_timestamp):
        payload = {
            'prop': str(property_value),
            'timestamp': str(property_timestamp),
            'thing_id': thing_id
        }

        print(payload)

        put_response = self.__kinesis_client.put_record(
            StreamName='streamrb',
            Data=json.dumps(payload),
            PartitionKey=thing_id)
