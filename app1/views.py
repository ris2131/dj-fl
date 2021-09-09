from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import userInfo
from .serializer import userInfoSerializer
import random

from django.shortcuts import render

from .findFeed.calculateFeed import calFeed

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


# BUG제안(inseok) : 안되는 id 넣으면 서버 터진다.
@api_view(['GET'])
def getUserInfo(request,id):
    #totalUserInfo = userInfo.objects.all()#되게 SQL 같다.
    uInfo = userInfo.objects.get(id=id) #get 이 있네 id=id 가 이상했는데 맞을까 했는데 되네. 앞 id 는 model 클래스의 id변수 , 뒤의 id는 파라미터로 받아오는 id 
    serializer = userInfoSerializer(uInfo)
    return Response(serializer.data)


#"IDs","name"을 body를 JSON 형태로 하나 받음.
#이를 JSON-> model userInfo로 변환 해서 이를 서버에 저장 해보려고 함.
@api_view(['POST'])
def inputUserInfo(request):
    user_info = userInfo() #넣어둘 모델var 미리 설정
    #user_info.IDs =request.POST['IDs']
    #user_info.IDs = userInfo.objects.count() + 1# 일어날 문제 : 고쳐줘야겠다. ID 삭제 하거나 하면 이게 중복 일어날 수 있겠다!!모르겠지만 여기 참고해보기https://jangwon.io/django/2018/02/20/(Django)-custom-autofield-%EA%B5%AC%ED%98%84/
    user_info.name = request.POST['name']
    user_info.pw = request.POST['pw']
    user_info.save()
    return Response("hello I'm Post")

#화면에 보여주는 역할
@api_view(['POST'])
def findFeed(request):
    #size = request.POST['size']#debug
    #여기서 def 를 하나 만들어서 계산해주는 back 을 하나 만들어 줄 예정
    #[def]calFeed : request 를 통해서 원하는 제품을 뽑아내주는 return (feedID, feedName 출력)
    feedInfo = calFeed(request)

    #return render(request,size)
    #return Response(feedInfo)
    return Response("hello")
##