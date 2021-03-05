def connection(access_tokens_file):
    from TwitterAPI import TwitterAPI
    from config.configuration import GlobalConfiguration

    conf = GlobalConfiguration(access_tokens_file)

    return TwitterAPI(conf.get_value('CONSUMER_KEY','tokens'),
                 conf.get_value('CONSUMER_SECRET','tokens'),
                 conf.get_value('ACCESS_TOKEN_KEY','tokens'),
                 conf.get_value('ACCESS_TOKEN_SECRET','tokens'))

def main(access_tokens_file):
    return connection(access_tokens_file)