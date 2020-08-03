#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:47 下午
# @Author  : lukegs7
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from rest_framework import routers
from aiops.views import EnvironmentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('environment', EnvironmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
