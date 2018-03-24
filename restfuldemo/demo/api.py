from demo.models import Stu
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class StuSerializer(serializers.ModelSerializer):
	class Meta:
		model=Stu
		fields='__all__'

@api_view(['GET','POST'])
def stu(request):
	if request.method=='GET':
		stu_list=Stu.objects.order_by('-id')
		serializer=StuSerializer(stu_list,many=True)
		return Response(serializer.data)

	elif request.method=='POST':
		serializer=StuSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






