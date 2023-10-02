from rest_framework import serializers
from .models import Ingredient, Recipe, Recipe_Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'