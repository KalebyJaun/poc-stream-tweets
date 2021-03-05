#!/usr/bin/env python
# -*- coding: utf-8 -*-

from connection import api_connection
from connection.kafka_connection import KafkaConnector
from exception.interruption_handler import GracefulInterruptHandler
from utility import save_tweet
import datetime
import uuid
import json
import sys

def stream(twitter, track_term, kafka, topic, path_to_save=None):    
    r = twitter.request('statuses/filter', {'track': track_term})

    with GracefulInterruptHandler() as h:
        for t in r:
            now = datetime.datetime.now()
            tweet = json.dumps(t)
            if path_to_save:
                save_tweet.save_to_path(tweet, str(now).replace(" ", "_").replace(":","").replace(".", "").replace("-", "") + '.json', path_to_save)
            kafka.produce(topic, str(uuid.uuid1()), tweet)
            if h.interrupted:
                kafka.flush_producer()
                sys.exit()


def main(conf):    
    access_tokens_file = conf.get_value('api_access_file', 'api')

    connection = api_connection.main(access_tokens_file)

    track_term = conf.get_value('track_term', 'api')

    kafka = KafkaConnector(conf.get_value('kafka_brokers_host', 'kafka'), conf.get_value('kafka_brokers_port', 'kafka'))

    stream(connection, track_term, kafka, conf.get_value('topic', 'kafka'))