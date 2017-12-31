from firstapp.models import Article
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

class ArticleSerializer(serializers.ModelSerializer):
		"""docstring for ClassName"""
		# validators可以加在min_length后面
		title=serializers.CharField(min_length=1)
		class Meta:
			model=Article
			fields="__all__"
			depth=1								#层级渲染


	#装饰器返回json 
	# articleapi=video
@api_view(['GET','POST'])
@authentication_classes((TokenAuthentication,))
def articleapi(request):
		print(request.user)
		print(request.auth)
		articleapi=Article.objects.order_by('-id')
		if request.method=='GET':
				if request.auth:
						serializer=ArticleSerializer(articleapi,many="True")		# 数据序列化
						return Response(serializer.data)	
				else:
						serializer=ArticleSerializer(articleapi[:5],many="True")		# 数据序列化
						return Response(serializer.data)	
																					# 返回数据
		elif request.method=='POST':
				# 类似表单
				serializer=ArticleSerializer(data=request.data)
				if serializer.is_valid():
						serializer.save()
						return Response(serializer.data,status=status.HTTP_201_CREATED)
				body={
					'body':serializer.errors,
					'msg':'40001'
				}
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@authentication_classes((TokenAuthentication,))
def article_card(request,id):
		article_card=Article.objects.get(id=id)
		if request.method=='PUT':
				serializer=ArticleSerializer(article_card,data=request.data)	
				if serializer.is_valid():
						serializer.save()
						return Response(serializer.data,status=status.HTTP_201_CREATED)
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

		# elif request.method=='DELETE':
		# 			article_card.delete()
		# 			return Response({'msg':'OK'},status=status.HTTP_201_CREATED)  

		# 创建者才可以删除
		elif request.method=='DELETE':
					if request.user.profile==article_card.owner:				#取得权限
							#UserProfile object
							print("---request.user.profile:--",request.user.profile)
							print("---article_card.owner:--",article_card.owner)
							# article_card.delete()
							return Response({'msg':'OK'},status=status.HTTP_201_CREATED)
					else:
							print("---request.user.profile:--",request.user.profile)
							print("---article_card.owner:--",article_card.owner)
							return Response({'msg':'Forbid'},status=status.HTTP_403_FORBIDDEN)