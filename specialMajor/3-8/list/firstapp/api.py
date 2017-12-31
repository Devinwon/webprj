from firstapp.models import Article
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ArticleSerializer(serializers.ModelSerializer):
		"""docstring for ClassName"""
		class Meta:
			model=Article
			fields="__all__"

	#装饰器返回json 
	# articleapi=video
@api_view(['GET'])
def articleapi(request):
		articleapi=Article.objects.all()
		serializer=ArticleSerializer(articleapi,many="True")		# 数据序列化
		return Response(serializer.data)												# 返回数据