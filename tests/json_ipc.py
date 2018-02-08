import unittest
import logging
import threading
import time
from kutils.json_ipc import JsonServerSocket, JsonClientSocket, JsonServerMaster, JsonServerProxy
from kutils.json_serialize import JsonSerializable

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
server_address = "test_json_ipc.socket"
ret = ""

class A(JsonSerializable):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def server_thread():
    server = JsonServerSocket(server_address, callback=server_callback)
    server.bind()
    try:
        while True:
            try:
                connection, client_address = server.accept()
                while connection.receive_call():
                    pass
            except Exception as e:
                logger.error("Error in control server: %s", e, exc_info=True)
                if connection is not None:
                    connection.close()
                server.reconnect()
    finally:
        server.close()

def server_callback(function, arguments):
    logger.info("received call: function=%s, arguments=%s", function, arguments)
    return arguments


def init_threads():
    server_worker = threading.Thread(target=server_thread)
    server_worker.setDaemon(True)
    server_worker.start()


def update_ret(new_ret):
    global ret
    ret = new_ret


class MyMaster(JsonServerMaster):
    def __init__(self, server_address):
        super().__init__(server_address, threaded=True)

    def test(self, **kwargs):
        return kwargs



class TestJsonIpc(unittest.TestCase):
    def test_json_ipc_3(self):
        # test_analysis('dummy', '196.200.181.7', '443' )
        master = MyMaster(server_address)
        # master.setDaemon(True)
        master.start()
        time.sleep(1)
        proxy = JsonServerProxy(server_address)

        r = proxy.test(**{'str':'long string dsjdksljddf s',
                                'bin':b'qdjkdkql\x00\x54\xf0\xffsdfqdfsjdiqierxbuiendfiosqf,iosq,io,aoidoisqjiodjijdijiofjookskqld',
                                'obj':A(1,2)})
        proxy.quit()
        master.stop()
        master.join()
        self.assertIsInstance(r['str'], str)
        self.assertIsInstance(r['bin'], bytes)
        self.assertIsInstance(r['obj'], A)

    def xtest_json_ipc_2(self):
        # test_analysis('dummy', '196.200.181.7', '443' )
        init_threads()
        time.sleep(5)
        client = JsonClientSocket(server_address)
        client.connect()
        r = client.call_function("test", {'str':'long string dsjdksljddf s',
                                          'bin':b'qdjkdkql\x00\x54\xf0\xffsdfqdfsjdiqierxbuiendfiosqf,iosq,io,aoidoisqjiodjijdijiofjookskqld',
                                          'obj':A(1,2)})
        client.quit()
        self.assertIsInstance(r['str'], str)
        self.assertIsInstance(r['bin'], bytes)
        self.assertIsInstance(r['obj'], A)

    def xtest_json_ipc(self):
        # test_analysis('dummy', '196.200.181.7', '443' )
        init_threads()
        time.sleep(5)
        client = JsonClientSocket(server_address)
        client.connect()
        update_ret(None)
        r = client.call_function("test", {'a':1, 'b':3})
        client.quit()
        self.assertEqual(r, None)



if __name__ == '__main__':
    unittest.main()