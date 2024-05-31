from django.urls import path
from .views import *

urlpatterns = [
    path('', MahsulotlarAPIView.as_view()),
]