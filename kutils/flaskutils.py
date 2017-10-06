from time import time as _time
from threading import Lock as _Lock
from kutils.string_ops import random_secure_string

import logging
logger = logging.getLogger(__name__)

MAX_CSRF_TOKEN_AGE = 600 # 10min
PURGE_RATE = 1200 # 20min
_mapping = None


class _CSRFMapping:
    def __init__(self):
        self._mapping = dict()
        self._purge_limit = _time() + MAX_CSRF_TOKEN_AGE
        self._lock = _Lock()

    def insert(self, form_id, referer, session_id, tmax, token):
        try:
            self._lock.aqcuire()
            self._insert(form_id, referer, session_id, tmax, token)
        finally:
            self._lock.release()

    def _insert(self, form_id, referer, session_id, tmax, token):
        t = _time()
        if t > self._purge_limit:
            self._purge()
        self._mapping[token] = (form_id, referer, session_id, t, tmax)


    def check(self, form_id, referer, session_id, token, tmax, unvalidate):
        try:
            self._lock.aqcuire()
            return self._check(form_id, referer, session_id, token, tmax, unvalidate)
        finally:
            self._lock.release()

    def _check(self, form_id, referer, session_id, token, tmax, unvalidate):
        t = _time()
        if t > self._purge_limit:
            self._purge()
        if token in self._mapping:
            form_id0, referer0, session_id0, t0, tmax = self._mapping[token]
            if (form_id0 is None or form_id0 == form_id) \
                    and (referer0 is None or referer0 == referer) \
                    and (session_id0 is None or session_id0 == session_id) \
                    and t < t0 + (MAX_CSRF_TOKEN_AGE if tmax is None else tmax):
                if unvalidate:
                    del self._mapping[token]
                return True
        return False


    def purge(self):
        try:
            self._lock.aqcuire()
            self._purge()
        finally:
            self._lock.release()

    def _purge(self):
        _to_remove = list()
        t = _time()
        for token in self._mapping:
            form_id0, referer0, session_id0, t0, tmax = self._mapping[token]
            if t > t0 + (MAX_CSRF_TOKEN_AGE if tmax is None else tmax):
                _to_remove.append(token)
        for token in _to_remove:
            del self._mapping[token]

def _get_csrf_mapping():
    global _mapping
    if _mapping == None:
        _mapping = _CSRFMapping()
    return _mapping

def get_csrf_token(form_id=None, referer=None, session_id=None, tmax=None):
    mapping = _get_csrf_mapping()
    token = random_secure_string()
    mapping.insert(form_id, referer, session_id, tmax, token)

def check_csrf_token(token, form_id=None , referer=None, session_id=None, unvalidate=True):
    mapping = _get_csrf_mapping()
    return mapping.check(form_id, referer, session_id, token,  unvalidate)



