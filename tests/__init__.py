from tests.useragent_test import *
from tests.flaskutils_test import *
from tests.urlselector_test import *
#from tests.crawler_test import * # TODO: fix crawler

import unittest


class TemplateTest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()