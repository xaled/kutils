import unittest
import logging
import threading
import time
from kutils.json_ipc import JsonServerSocket, JsonClientSocket

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
server_address = "test_json_ipc.socket"
ret = ""


def server_thread():
    server = JsonServerSocket(server_address, callback=server_callback)
    server.bind()
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


def server_callback(function, arguments):
    logger.info("received call: function=%s, arguments=%s", function, arguments)
    return ret


def init_threads():
    server_worker = threading.Thread(target=server_thread)
    server_worker.setDaemon(True)
    server_worker.start()


def update_ret(new_ret):
    global ret
    ret = new_ret


class TestJsonIpc(unittest.TestCase):
    def test_json_ipc(self):
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