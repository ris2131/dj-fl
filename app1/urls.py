from django.urls import path, include
from .views import  helloAPI, randomUserInfo,inputUserInfo, getUserInfo, findFeed #내가 만든 함수

urlpatterns =[
    path("hello/", helloAPI),
    path("<int:id>/", randomUserInfo),
    #path("random/<int:id>/", randomUserInfo),
    path("inputUserInfo/",inputUserInfo),
    path("getId/<int:id>",getUserInfo),
    path("findFeed",findFeed),
    #inputFeedInfo
    #testFeedInfo
]

