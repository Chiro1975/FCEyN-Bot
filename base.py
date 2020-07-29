#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pony.orm import *

db = Database()


class Command(db.Entity):
    name = Required(str)
    enabled = Required(bool, default=True)


class ListableFisica(db.Entity):
    name = Required(str)
    url = Required(str)
    validated = Required(bool, default=False)

class ListableMatematica(db.Entity):
    name = Required(str)
    url = Required(str)
    validated = Required(bool, default=False)


class ListableMatematicaOptativa(db.Entity):
    name = Required(str)
    url = Required(str)
    validated = Required(bool, default=False)          


class File(db.Entity):
    path = Required(str)
    file_id = Required(str)


def init_db(path):
    db.bind('sqlite', path, create_db=True)
    db.generate_mapping(create_tables=True)