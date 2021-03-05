def save_to_path(tweet, output_file, path):
    with open(path + output_file, 'w') as out:
        out.write(str(tweet))
    print('saved ' + output_file)
