import os
from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
    return HttpResponse("status ok")

def onRequest(request):
    return HttpResponse("wait for app")

def onWxRequest(request):
    return HttpResponse("wait for wx")
