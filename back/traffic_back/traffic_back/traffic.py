#!/usr/bin/env python
#coding=utf-8

import numpy as np
import datetime
from traffic_back.db import get_db


def read_last(period=24):
    db = get_db()
    fields = ('timestamp', 'debit', 'percent')
    with db.cursor() as cursor:
        cursor.execute("SELECT timestamp, debit, percent FROM traffic ORDER BY timestamp DESC LIMIT %s;", (period,))
        data = cursor.fetchall()
        data_dict = [dict(zip(fields, row)) for row in data] 
        print(data)
    return {'data' : data_dict}
