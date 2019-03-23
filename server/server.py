import asyncio
import os
import uvloop


class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.loop = asyncio.get_event_loop()
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def subserver_start(self, loop):
        await asyncio.start_server(self.handler.handle, self.host, self.port, loop=loop, reuse_port=True)

    def start(self, cpu, threads):
        subservers = []
        for i in range(cpu):
            pid = os.fork()
            subservers.append(pid)
            if pid == 0:
                # loop = asyncio.get_event_loop()
                for j in range(threads):
                    self.loop.create_task(self.subserver_start(self.loop))
                self.loop.run_forever()
        print('subservers: ', subservers)
        for pid in subservers:
            os.waitpid(pid, 0)

    def stop(self):
        self.loop.stop()
