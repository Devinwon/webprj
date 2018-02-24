from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import Template,Context
# Create your views here.
def query(request):
	if request.method=="GET":
		return render(request,'people/query.html',{})

def add(request):
	return render()