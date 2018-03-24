from django.shortcuts import render
from demo.models import Stu
from django.http import HttpResponse

# Create your views here.

def index(request):
	context={}
	if request.method=='GET':
		stu=Stu.objects.all()
		context['stu']=stu
		return render(request,'index.html',context)
	else:
		name=request.POST.get("name",None)
		tel=request.POST.get("tel",None)
		if name  and tel:
			Stu.objects.create(name=name,tel=tel)
			return HttpResponse("Success")
		else:
			return HttpResponse("Error")


