from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import userInfo
from .serializer import userInfoSerializer
import random
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello I'm Django")

#21/08/31 inseok : request,id 가 뭔지 잘 모르겠음.
#갯수를 넣어주면 그만큼 랜덤한 userInfo 반환(추첨 생각해보면 의미 있을듯.)
#random id와 name (회원 정보) Get 해볼 생각.(randomQuiz 비슷하게)
#many = true : 다량의 데이타 직렬화
@api_view(['GET'])
def randomUserInfo(request, id):
    totalUserInfo = userInfo.objects.all()#되게 SQL 같다.
    randomUserInfo = random.sample(list(totalUserInfo), id)
    serializer = userInfoSerializer(randomUserInfo, many=True)
    return Response(serializer.data)
    #return Response(id)