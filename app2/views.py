from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def month (request):
    return HttpResponse('hii this month is november')