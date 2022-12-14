"""iou_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from iou.views import UserViewSet,UserCreateViewSet,IouCreateViewset
from rest_framework import routers
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'settleup', UserViewSet)
router.register('add',UserCreateViewSet)
router.register('iou',IouCreateViewset)
schema_view = get_swagger_view(title='IOU API')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r"expired_iou", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(r'docs', schema_view)
]
