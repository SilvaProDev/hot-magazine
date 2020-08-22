from rest_framework import serializers
from home import models


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.ContactMessage
        fields= '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Produit
        fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):
    produit= ProduitSerializer(many=True, required=False)
    class Meta:
        model= models.Category
        fields= '__all__'