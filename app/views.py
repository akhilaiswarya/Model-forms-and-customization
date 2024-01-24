from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done successfully')
        
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EFWO=WebPageForm()
    d={'EFWO':EFWO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is done successfully')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EFAO=AccessRecordForm()
    d={'EFAO':EFAO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_accessrecord is done successfully')

    return render(request,'insert_accessrecord.html',d)
