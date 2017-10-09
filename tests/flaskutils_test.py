import kutils.flaskutils as fu
import logging
logging.basicConfig(level=logging.DEBUG)


csrf_token = fu.get_csrf_token()
print csrf_token
print fu.check_csrf_token(csrf_token)
print fu.check_csrf_token(csrf_token)
csrf_token = fu.get_csrf_token(form_id="form1")
print csrf_token
print fu.check_csrf_token(csrf_token)
print fu.check_csrf_token(csrf_token, form_id="form1")
print fu.check_csrf_token(csrf_token, form_id="form1")

csrf_token = fu.get_csrf_token(form_id="form2", referer="page1", session_id="user1")
print csrf_token
print fu.check_csrf_token(csrf_token)
print fu.check_csrf_token(csrf_token, form_id="form1", referer="page1", session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form2", referer="page2", session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user2")
print fu.check_csrf_token(csrf_token, form_id=None, referer="page1", session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form2", referer=None, session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id=None)
print fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form2", referer="page1", session_id="user1")