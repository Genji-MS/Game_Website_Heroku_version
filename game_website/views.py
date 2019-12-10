from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index_text.html')
    #return HttpResponse(index.html)