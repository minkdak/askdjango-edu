# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render


'''

    def mysum(request, x, y=0, z=0):
    # request: HttpRequest
    return HttpResponse(int(x) + int(y) + int(z))
'''

def mysum(request, numbers):
    # request: HttpRequest
    # numbers = "1/2/12/123/12321/321/1232313"

    result = sum(list(map(lambda s: int(s or 0), numbers.split("/"))))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {} 살이시네요'.format(name, age))
