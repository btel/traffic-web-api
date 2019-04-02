#!/usr/bin/env python
#coding=utf-8

import pandas as pd
from flask import current_app, g
import click
from . import db
from flask.cli import with_appcontext
import psycopg2 as pg
import logging
from dateutil import parser

@click.command("import-traffic")
@click.argument('csv_files', nargs=-1)
@with_appcontext
def import_traffic_command(csv_files):
    "import traffic from csv files"

    for filename in csv_files:
        df = pd.read_csv(filename, 
                         decimal=b',', sep='\t', 
                         names=['arc_id', 'date', 'debit', 'percent'],
                         parse_dates=True)
        df = df[df.arc_id == 1] 

        conn = db.get_db()
        conn.autocommit = True
        with conn.cursor() as cursor:
            for row in df.itertuples():
                date = parser.parse(row.date)
                try:
                    cursor.execute("INSERT INTO traffic (timestamp, debit, percent) VALUES (%s, %s, %s)", (date.isoformat(), row.debit, row.percent))
                except pg.DataError:
                    logging.warn('skipping row %s due to import error', row)



def init_app(app):
    app.cli.add_command(import_traffic_command)
