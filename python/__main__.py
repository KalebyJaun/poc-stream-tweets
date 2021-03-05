if __name__ == '__main__':
    from utility import functions
    from stream.stream_tweets import main as stream_main
    from config.configuration import GlobalConfiguration

    conf = GlobalConfiguration('/home/kalebyjaun/stream-tweets/python/config/stream_tweets.cfg')

    stream_main(conf)