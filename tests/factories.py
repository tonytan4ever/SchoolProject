# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    Overholt test factories module
"""

from datetime import datetime

from factory import Factory, Sequence, LazyAttribute
from flask_security.utils import encrypt_password

from framework.core import db
from framework.models import *


def create_sqlalchemy_model_function(class_to_create, *args, **kwargs):
    entity = class_to_create(**kwargs)
    db.session.add(entity)
    db.session.commit()
    return entity

Factory.set_creation_function(create_sqlalchemy_model_function)


class RoleFactory(Factory):
    FACTORY_FOR = Role
    name = 'admin'
    description = 'Administrator'


class UserFactory(Factory):
    FACTORY_FOR = User
    email = Sequence(lambda n: 'user{0}@overholt.com'.format(n))
    password = LazyAttribute(lambda a: encrypt_password('password'))
    last_login_at = datetime.utcnow()
    current_login_at = datetime.utcnow()
    last_login_ip = '127.0.0.1'
    current_login_ip = '127.0.0.1'
    login_count = 1
    roles = LazyAttribute(lambda _: [RoleFactory()])
    active = True

