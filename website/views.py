from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse('Welcome')


def date(request):
    return HttpResponse('This page was serve at ' + str(datetime.now()))


def about(request):
    return HttpResponse('About')
