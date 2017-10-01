"""Minimalistic Json database.
:Date: 2002-03-22
:Version: 1
:Authors:
    - Me
    - Myself
    - I"""

__license__ = "MIT License"
__docformat__ = 'reStructuredText'
__author__ = "xaled"



import os
import json


def _load_json(path ):
    with open(path) as fin:
        return json.load(fin)


def _save_json(data, path, indent=None):
    with open(path, 'w') as fou:
        json.dump(data, fou, indent=indent)

class JsonMinConnexion:
    """Minimalistic Json Database Connexion class."""

    def __init__(self, path, create=True, template=None, template_file=None, indent=3):
        """JsonMinDb constructor.

        :param path: json file path.
        :type name: str.
        :param create: Create if json file does not exist.
        :type create: bool.
        :param template: if create is True, create from template.
        :type template: dict.
        :param template_file: if create is True and template is None, create from template_file.
        :type template_file: str.
        :param indent: if create is True, create from template.
        :type indent: int.
        :raises: ValueError

        """
        self.path = path
        self.indent = indent


        if not os.path.isfile(path):
            if create:
                if template:
                    _template = template
                elif template_file:
                    _template = _load_json(template_file)
                else:
                    _template = {}

                _save_json(_template, path, indent=indent)
                self.db = _load_json(path)
            else:
                raise ValueError("Database file doesn't exist: " + path)
        self.db = _load_json(path)

        # db dict calls
        self.__contains__ = self.db.__contains__
        self.__delitem__ = self.db.__delitem__
        self.__getitem__ = self.db.__getitem__
        self.__iter__ = self.db.__iter__
        self.__len__ = self.db.__len__
        self.__setitem__ = self.db.__setitem__

        #self.clear = self.db.clear
        #self.copy = self.db.copy
        #self.fromkeys = self.db.fromkeys
        self.has_key = self.db.has_key
        self.items = self.db.items
        self.iteritems = self.db.iteritems
        self.iterkeys = self.db.iterkeys
        self.itervalues = self.db.itervalues
        self.keys = self.db.keys
        self.update = self.db.update
        self.values = self.db.values


    def save(self):
        """updates database persistance file in the disk. """
        _save_json(self.db, self.path, indent=self.indent)

    def reload(self):
        """reload database from disk."""
        self.db = _load_json(self.path)

    def __str__(self):
        return "<kutils.json_min_db.JsonMinConnexion instance %s>" % self.db.__str__()