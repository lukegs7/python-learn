from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from aiops.models import Environment
from aiops.serializers import EnvironmentSerializer
from commons.custom_viewset import CustomViewBase


class EnvironmentViewSet(CustomViewBase):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    parser_classes = (JSONParser,)
