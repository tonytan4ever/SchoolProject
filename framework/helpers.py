# -*- coding: utf-8 -*-
"""
    framework.helpers
    ~~~~~~~~~~~~~~~~

    social_framework helpers module
"""

import pkgutil
import importlib

from flask import Blueprint
from flask.json import JSONEncoder as BaseJSONEncoder


def register_blueprints(app, subapp_names):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param subapp_names: a list of subapps to be registered as Blueprint. 
          Assumption: every submodule should have a bp attribute that is 
                      registerable as Blueprint
    """
    rv = []
    for subapp in subapp_names:
        m = importlib.import_module('%s' % (subapp))
        bp = getattr(m, 'bp', None)
        if bp is not None and isinstance(bp, Blueprint):
            app.register_blueprint(bp)
    return rv


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.get_field_names()

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv