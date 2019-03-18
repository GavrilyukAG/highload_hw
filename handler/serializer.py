from models.response import Response


class Serializer:
    def __init__(self):
        pass

    @staticmethod
    async def dump(response):
        if response.status == Response.OK:
            return Serializer.good_resp(response).encode() + response.body
        else:
            return Serializer.bad_resp(response).encode()

    @staticmethod
    def good_resp(response):
        return "{} {}\r\n" \
               "Server: {}\r\n" \
               "Date: {}\r\n" \
               "Connection: {}\r\n" \
               "Content-Length: {}\r\n" \
               "Content-Type: {}\r\n\r\n".format(response.protocol, response.status, response.server, response.date,
                                                 response.connection, response.content_length, response.content_type)

    @staticmethod
    def bad_resp(response):
        return "{} {}\r\n" \
               "Server: {}\r\n" \
               "Date: {}\r\n" \
               "Connection: {}\r\n\r\n".format(response.protocol, response.status, response.server, response.date,
                                               response.connection)
