from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello world! I am coming...")



'''
def hello (request):
	return render(request,'new.html')
'''