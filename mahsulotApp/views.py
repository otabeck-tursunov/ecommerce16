from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *

from .models import *
from .serializers import *
from userApp.permissions import *


class MahsulotlarAPIView(APIView):
    def get(self, request):
        mahsulotlar = Mahsulot.objects.all()

        katalog = request.query_params.get('katalog', None)
        if katalog is not None:
            katalog = get_object_or_404(Katalog, id=katalog)
            mahsulotlar = mahsulotlar.filter(subKatalog__katalog=katalog)

        subKatalog = request.query_params.get('subKatalog', None)
        if subKatalog is not None:
            subKatalog = get_object_or_404(SubKatalog, id=subKatalog)
            mahsulotlar = mahsulotlar.filter(subKatalog=subKatalog)

        brend = request.query_params.get('brend', None)
        if brend is not None:
            mahsulotlar = mahsulotlar.filter(brend=brend)

        min_narx = request.query_params.get('min_narx', None)
        if min_narx is not None:
            mahsulotlar = mahsulotlar.filter(narx__gte=min_narx)  # __gt -> ">", __gte -> ">="

        max_narx = request.query_params.get('max_narx', None)
        if max_narx is not None:
            mahsulotlar = mahsulotlar.filter(narx__lte=max_narx)

        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)
