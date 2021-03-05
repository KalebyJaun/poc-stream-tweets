if __name__ == '__main__':
    from utility import functions
    from stream.stream_tweets import main as stream_main
    from config.configuration import GlobalConfiguration
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--config-file', action = 'store', dest = 'config_file', required = True,
                           help = 'caminho absoluto para o arquivo de configuracao')
    arguments = parser.parse_args()

    conf = GlobalConfiguration(arguments.config_file)

    stream_main(conf)