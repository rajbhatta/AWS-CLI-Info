import json

import boto3 as boto3

class Consumer():

    def __init__(self):
        """

        1. Create connection with kinesis
        2. Describe kinesis stream
        3. Select shard ID
        4. Get shard iterator
        5. Get record

        """
        self.__stream_name = 'streamrb'
        self.__kinesis_client = boto3.client('kinesis', region_name='us-west-2')
        self.__kinesis_response = self.__kinesis_client.describe_stream(StreamName=self.__stream_name)
        self.__shard_id =  self.__kinesis_response['StreamDescription']['Shards'][0]['ShardId']

        self.__shard_iterator = self.__kinesis_client.get_shard_iterator(StreamName=self.__stream_name,
                                                           ShardId=self.__shard_id,
                                                           ShardIteratorType='LATEST')

        self.__my_shard_iterator = self.__shard_iterator['ShardIterator']
        self.__record_response = self.__kinesis_client.get_records(ShardIterator=self.__my_shard_iterator,
                                                     Limit=2)


    def return_stream_response(self):
        while 'NextShardIterator' in self.__record_response:
            record_response = self.__kinesis_client.get_records(ShardIterator= self.__record_response['NextShardIterator'],
                                                         Limit=2)
            return record_response
