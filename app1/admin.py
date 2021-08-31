from django.contrib import admin
from .models import userInfo
# Register your models here.

#관리자 페이지에 app1 모델을 register 하여 관리 할수 있도록 처리.
admin.site.register(userInfo)