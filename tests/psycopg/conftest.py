import pytest
import psycopg2
import os
from mobilitydb import *
from mobilitydb.psycopg import register

db = psycopg2.connect(dbname=os.getenv('PGDATABASE', 'test'))
db.autocommit = True

register(db)
cur = db.cursor()

time_types = [TimestampSet, Period, PeriodSet]
box_types = [TBox, STBox]
subtype_suffixes = ['Inst', 'InstSet', 'Seq', 'SeqSet']
subtype_names = ['INSTANT', 'INSTANTSET', 'SEQUENCE', 'SEQUENCESET']
temporal_types = [TBool, TInt, TFloat, TText, TGeomPoint, TGeogPoint]

def pytest_configure():
    for time in time_types:
        cur.execute(
            'CREATE TABLE IF NOT EXISTS tbl_' + time.__name__.lower() +
            '(timetype ' +  time.__name__.lower() + ' NOT NULL);')
    for box in box_types:
        cur.execute(
            'CREATE TABLE IF NOT EXISTS tbl_' + box.__name__.lower() +
            '(box ' +  box.__name__.lower() + ' NOT NULL);')
    for ttype in temporal_types:
        for suffix, name in zip(subtype_suffixes, subtype_names):
            cur.execute(
                'CREATE TABLE IF NOT EXISTS tbl_' + ttype.__name__.lower() + suffix +
                '(temp ' + ttype.__name__.lower() + '(' + name + ') NOT NULL);')

def pytest_unconfigure():
    for time in time_types:
        cur.execute(
            'DROP TABLE tbl_' + time.__name__.lower() + ';')
    for box in box_types:
        cur.execute(
            'DROP TABLE tbl_' + box.__name__.lower() + ';')
    for ttype, suffix in zip(temporal_types, subtype_suffixes):
        cur.execute('DROP TABLE tbl_' + ttype.__name__.lower() + suffix + ';')

@pytest.fixture
def cursor():
    # Make sure tables are clean.
    for time in time_types:
        cur.execute('TRUNCATE TABLE tbl_' + time.__name__.lower() + ';')
    for box in box_types:
        cur.execute('TRUNCATE TABLE tbl_' + box.__name__.lower() + ';')
    for ttype in temporal_types:
        for suffix in subtype_suffixes:
            cur.execute('TRUNCATE TABLE tbl_' + ttype.__name__.lower() + suffix + ';')
    return cur
