#!/usr/bin/env python
# -*- coding: utf-8 -*-
def get_csv(text, user_name, user_location, user_lang):
    return("'" + text + "'|'" + user_name + "'|'" + user_location + "'|'" + user_lang + "'")

def get_tweet_info(tweet):
    try:
        text = tweet["text"].encode("utf-8").replace("\n", "")
    except AttributeError:
        text = ""
    try:
        user_name = tweet["user"]["name"].encode("utf-8").replace("\n", "")
    except AttributeError:
        user_name = ""
    try:
        user_location = tweet["user"]["location"].encode("utf-8").replace("\n", "")
    except AttributeError:
        user_location = ""
    try:
        user_lang = tweet["user"]["lang"].encode("utf-8").replace("\n", "")
    except AttributeError:
        user_lang = ""
    return get_csv(text, user_name, user_location, user_lang)

def stream(twitter, kafka, topic, path_to_save):
    from utility import save_tweet
    import datetime
    import uuid
    import json

    TRACK_TERM = '#HoldOn'
    r = twitter.request('statuses/filter', {'track': TRACK_TERM})

    for t in r:
        now = datetime.datetime.now()
        tweet = json.dumps(t)
        #save_tweet.save_to_path(tweet, str(now).replace(" ", "_").replace(":","").replace(".", "").replace("-", "") + '.json', path_to_save)
        kafka.produce(topic, str(uuid.uuid1()), tweet)


def main(conf):
    from connection import api_connection
    from connection.kafka_connection import KafkaConnector
    
    access_tokens_file = conf.get_value('api_access_file', 'api')

    connection = api_connection.main(access_tokens_file)    

    kafka = KafkaConnector(conf.get_value('kafka_brokers_host', 'kafka'), conf.get_value('kafka_brokers_port', 'kafka'))

    stream(connection, kafka, conf.get_value('topic', 'kafka'), '/home/kalebyjaun/twitter/collected-tweets/')