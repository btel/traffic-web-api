#!/usr/bin/env python
#coding=utf-8

import numpy as np
import datetime


def read_last(period=24):
    now = datetime.datetime.utcnow()
    hour = datetime.timedelta(hours=1)
    dates = [now - i * hour for i in range(period)]
    debit = np.random.randint(0, 100, size=100).tolist()
    percent = (np.random.rand(100) * 100).tolist()

    data = []
    for date, dd, pp in zip(dates, debit, percent):
        data.append(dict(date=date, debit=dd, percent=pp))
    return {'data' : data}
