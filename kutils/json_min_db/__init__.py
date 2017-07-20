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

    def __init__(self, path, create=True, template=None, indent=3):
        """JsonMinDb constructor.

        :param path: json file path.
        :type name: str.
        :param create: Create if json file does not exist.
        :type create: bool.
        :param template: if create is True, create from template.
        :type template: dict.
        :param indent: if create is True, create from template.
        :type indent: int.
        :raises: ValueError

        """
        self.path = path
        self.indent = indent

        if not os.path.isfile(path):
            if create:
                _template = {}
                if template:
                    _template = template

                _save_json(_template, path, indent=indent)
                self.db = _load_json(path)
            else:
                raise ValueError("Database file doesn't exist: " + path)
        self.db = _load_json(path)

    def save(self):
        """updates database persistance file in the disk. """
        _save_json(self.db, self.path, indent=self.indent)

    def reload(self):
        """reload database from disk."""
        self.db = _load_json(self.path)
