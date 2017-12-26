from __future__ import print_function
import kutils.net
import unittest


class UserAgentTest(unittest.TestCase):
    def testUniq(self):
        ua_set = set()
        for i in range(100):
            ua = kutils.net.get_useragent()
            print(ua)
            ua_set.add(ua)
        self.assertGreater(len(ua_set), 70)
