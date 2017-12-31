from firstapp.models  import Student
from django.shortcuts import render,redirect

def student(request):
		if request.method=='POST':
				# 获取表单字段的不同方式
				name=request.POST['name']
				address=request.POST['address']
				website=request.POST.get('website')

				# 新建并保存
				Student.objects.create(
					name=name,
					address=address,
					website=website,
					)
				return render(request,'test.html',{})

		elif request.method=='GET':
				return render(request,'test.html',{})