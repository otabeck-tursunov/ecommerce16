from django.contrib import admin
from .models import *

admin.site.register([Katalog, SubKatalog, Mahsulot, Rasm, Xususiyat, Rate])
