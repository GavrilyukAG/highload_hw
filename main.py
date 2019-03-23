from config_reader.config_reader import read_file
from server.server import Server
from handler.handler import Handler


if __name__ == '__main__':
    config = read_file('httpd.conf')
    # config = read_file('test_conf.conf')
    print(config)
    handler = Handler(config['files'])
    server = Server(config['host'], config['port'], handler)
    try:
        server.start(int(config['cpu']), int(config['threads']))
        print('Server started')
    except KeyboardInterrupt:
        server.stop()
        print('Server stopped')
