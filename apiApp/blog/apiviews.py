from rest_framework import viewsets
from .serializers import *
from home import models


class ContactMessageViewset(viewsets.ModelViewSet):
    queryset = models.ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class ProduitViewset(viewsets.ModelViewSet):
    queryset = models.Produit.objects.all()
    serializer_class = ProduitSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer