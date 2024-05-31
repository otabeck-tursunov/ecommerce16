from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from coreApp.models import CoreModel
from userApp.models import User


class Katalog(CoreModel):
    sarlavha = models.CharField(max_length=255, unique=True)
    rasm = models.ImageField(upload_to='kataloglar/')

    def __str__(self):
        return self.sarlavha


class SubKatalog(CoreModel):
    sarlavha = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='sub-kataloglar/')
    katalog = models.ForeignKey(Katalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha


class Mahsulot(CoreModel):
    nom = models.CharField(max_length=255)
    batafsil = models.TextField(blank=True, null=True)
    brend = models.CharField(max_length=255, blank=True)
    dokon = models.CharField(max_length=255, blank=True)
    narx = models.FloatField(validators=[MinValueValidator(0)])
    chegirma = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    miqdor = models.PositiveIntegerField(default=1)
    kafolat = models.CharField(max_length=255, blank=True, null=True)
    baho = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    subKatalog = models.ForeignKey(SubKatalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Rasm(CoreModel):
    rasm = models.ImageField(upload_to='mahsulotlar/')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rasm: {self.mahsulot.nom}"


class Xususiyat(CoreModel):
    nom = models.CharField(max_length=255)
    qiymat = models.CharField(max_length=255)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("qiymat", "nom"),)

    def __str__(self):
        return f"{self.nom}: {self.qiymat} | {self.mahsulot.nom}"


class Rate(CoreModel):
    baho = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    izoh = models.TextField(blank=True, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("mahsulot", "user"), )
