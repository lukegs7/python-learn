#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 10:37 下午
# @Author  : lukegs7
# @File    : serializers.py
# @Software: PyCharm
from aiops.models import *
from rest_framework import serializers


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'
