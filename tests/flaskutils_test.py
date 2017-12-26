from __future__ import print_function
import kutils.flaskutils as fu
import unittest


class CSRFTokenTest(unittest.TestCase):
    def testTokenWithoutConstraints(self):
        csrf_token = fu.get_csrf_token()
        print(csrf_token)
        self.assertTrue(fu.check_csrf_token(csrf_token))
        self.assertFalse(fu.check_csrf_token(csrf_token))

    def testTokenWithFormIdConstraint(self):
        csrf_token = fu.get_csrf_token(form_id="form1")
        print(csrf_token)
        self.assertFalse(fu.check_csrf_token(csrf_token))
        self.assertTrue(fu.check_csrf_token(csrf_token, form_id="form1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form1"))

    def testTokenWithAllConstraints(self):
        csrf_token = fu.get_csrf_token(form_id="form2", referer="page1", session_id="user1")
        print(csrf_token)
        self.assertFalse(fu.check_csrf_token(csrf_token))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form1", referer="page1", session_id="user1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form2", referer="page2", session_id="user1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user2"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id=None, referer="page1", session_id="user1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form2", referer=None, session_id="user1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id=None))
        self.assertTrue(fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user1"))
        self.assertFalse(fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user1"))



