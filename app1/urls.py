from django.urls import path, include
from .views import  getUserInfo, helloAPI, randomUserInfo,inputUserInfo #내가 만든 함수

urlpatterns =[
    path("hello/", helloAPI),
    path("<int:id>/", randomUserInfo),
    #path("random/<int:id>/", randomUserInfo),
    path("inputUserInfo/",inputUserInfo),
    path("getId/<int:id>",getUserInfo),
    #inputFeedInfo
    #testFeedInfo
]

