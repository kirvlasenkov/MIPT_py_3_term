import asyncio


class Storage:
    def __init__(self):
        self.__metrics_dict = {}

    def put(self, key, value, timestamp):
        if not (key in self.__metrics_dict.keys()):
            self.__metrics_dict[key] = {}
        self.__metrics_dict[key][timestamp] = value

    def get(self, key):
        temp_data = self.__metrics_dict
        if key != '*':
            temp_data = {
                key: temp_data.get(key, {})
            }
        result = {}
        for key, timestamp in temp_data.items():
            result[key] = sorted(timestamp.items())
        return result


class ReadError(ValueError):
    pass


class Parser:

    def decoding(self, responses):
        messages = []
        for response in responses:
            if response:
                for key, timestamp_dict in response.items():
                    for timestamp, value in timestamp_dict:
                        messages.append("{} {} {}".format(key, value, timestamp))
        ret_msg = 'ok\n'
        if len(messages) > 0:
            ret_msg += '\n'.join(messages) + '\n'
        ret_msg += '\n'
        return ret_msg

    def encoding(self, req):
        try:
            parts = req.split('\n')
            parts = list([part for part in parts if len(part) > 0])
            if len(parts) == 0:
                raise ValueError('error: invalid method')
        except ValueError:
            raise ReadError('wrong command')

        commands = []
        for part in parts:
            try:
                method, params = part.strip().split(" ", 1)
                if method == 'put':
                    if len(params.split(' ')) != 3:
                        raise ValueError('error: invalid method')
                    key, value, timestamp = params.split(' ')
                    if key.isnumeric():
                        raise ValueError('error: invalid method')
                    commands.append((method, key, float(value), int(timestamp)))
                elif method == 'get':
                    if len(params.split(' ')) != 1:
                        raise ValueError('error: invalid method')
                    key = params
                    if key.isnumeric():
                        raise ValueError('error: invalid method')
                    commands.append((method, key))
                else:
                    raise ValueError('error: invalid method')
            except ValueError:
                raise ReadError('wrong command')
        return commands


class ExecuteError(Exception):
    pass


class Executor:
    def __init__(self, metrics_storage):
        self.metrics_storage = metrics_storage

    def run(self, method, *params):
        if method == 'put':
            return self.metrics_storage.put(*params)
        elif method == 'get':
            return self.metrics_storage.get(*params)
        else:
            raise ExecuteError('invalid method')


class ClientServerProtocol(asyncio.Protocol):
    metrics_storage = Storage()

    def __init__(self):
        super().__init__()

        self.parser = Parser()
        self.executor = Executor(self.metrics_storage)
        self.buffer = b''

    def process_data(self, req):
        cmds = self.parser.encoding(req)
        responses = []
        for cmd in cmds:
            res = self.executor.run(*cmd)
            responses.append(res)
        return self.parser.decoding(responses)

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, req):
        self.buffer += req
        try:
            decoded_req = self.buffer.decode()
        except UnicodeError:
            return

        if not decoded_req.endswith('\n'):
            return

        self.buffer = b''

        try:
            res = self.process_data(decoded_req)
        except(ReadError, ExecuteError) as e:
            self.transport.write('error\n{}\n\n'.format(e).encode())
            return
        self.transport.write(res.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
