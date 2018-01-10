from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse
import os

from django.template import Template,Context


# Create your views here.
def msgproc(request):
	datalist=[]
	if request.method=="POST":
		userA=request.POST.get("userA",None)
		userB=request.POST.get("userB",None)
		msg=request.POST.get("msg",None)
		time=datetime.now()
		# 'a+',没有就自动建立文件
		with open("msgdata.txt",'a+') as f:
			f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))


	if request.method=="GET":
		
		with open("msgdata.txt","r") as f:
			for line in f:
				linedata=line.split('--')
				d={"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
				datalist.append(d)
	return render(request,"MsgSingleWeb.html",{"data":datalist})

'''
	if request.method=="GET":
		userC=request.GET.get("userC",None)
		if userC!=None:
			with open("msgdata.txt","r") as f:
				cnt=0
				for line in f:
					linedata=line.split('--')
					if linedata[0]==userC:
						cnt=cnt+1
						d={"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
						datalist.append(d)
					if cnt>=10:
						break
	return render(request,"MsgSingleWeb.html",{"data":datalist})
'''

def  testindex(request):
	if request.method=="GET":
		return render(request,"testindex.html")


def testjson(request):
	response=JsonResponse({'key':'value1',})
	return response

# 提示保存文件
def testfile(request):
	cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	response=FileResponse(open(cwd+'/msgapp/templates/pic.png',"rb"))
	response['Content-Type']='application/octet-stream'
	response['Content-Disposition']='attachment;filename="pic.png"'
	return response


def testtemp(request):
	template=Template("<h1>这个程序的名字是{{name }}</h1>")
	context=Context({'name':'实验平台'})
	return HttpResponse(template.render(context))
