from django.urls import path
from WebPage.views import *

urlpatterns = [
    path('inicio/', index)
]