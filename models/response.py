from datetime import datetime


class Response:
    OK = '200 OK'
    NOT_FOUND = '404 NOT FOUND'
    METHOD_NOT_ALLOWED = '405 NOT ALLOWED'
    FORBIDDEN = '403 FORBIDDEN'

    today_date = datetime.today()

    def __init__(self, status, protocol, connection, content_type='', content_length=0, body=b''):
        self.status = status
        self.protocol = protocol.decode()
        self.connection = connection
        self.content_type = content_type
        self.content_length = content_length
        self.body = body
        self.server = "server"
        self.date = Response.today_date.strftime("%a, %d %b %Y %H:%M:%S %Z")

    def get_connection(self):
        return self.connection

    def get_status(self):
        return self.status

    def get_protocol(self):
        return self.protocol

    def get_content_type(self):
        return self.content_type

    def get_content_length(self):
        return self.content_length

    def get_body(self):
        return self.body
