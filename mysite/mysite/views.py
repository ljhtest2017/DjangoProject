#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: liuJiahai
# Time: 2019/12/13 14:57

import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "It is now %s" % now
    #     # return HttpResponse(html)
    return render(request, 'mysite/current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be %s." % (offset, dt)
    return HttpResponse(html)