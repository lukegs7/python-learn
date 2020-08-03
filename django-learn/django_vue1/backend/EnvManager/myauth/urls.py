from django.urls import path, include

from .views import *

urlpatterns = [
    path('login', ProLoginView.as_view()),
    path('user/info', UserInfoViewSet.as_view())
]
