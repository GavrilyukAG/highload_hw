class Request:
    def __init__(self, method, protocol, url, connection):
        self.method = method
        self.protocol = protocol
        self.url = url
        self.connection = connection

    def get_method(self):
        return self.method

    def get_protocol(self):
        return self.protocol

    def get_url(self):
        return self.url

    def get_connection(self):
        return self.connection


def get_values(data):
    arr = data.split(b'\n')
    values = arr[0].split()
    method = values[0]
    query = values[1].split(b'?')[0]
    protocol = values[2]
    return Request(method, protocol, query, '')
