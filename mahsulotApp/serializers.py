from rest_framework.serializers import ModelSerializer
from .models import *


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'
