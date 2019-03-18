def read_file(name):
    file = open(name, 'r')
    config = dict.fromkeys(['host', 'port', 'cpu', 'threads', 'files'])
    for line in file:
        words = (' '.join(line.split())).split(' ')
        if words[0] in config.keys():
            config[words[0]] = words[1]

    if None in config.values():
        print('There is an important value missing in config')
        return 0

    return config
