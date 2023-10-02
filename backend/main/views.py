from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from .models import Ingredient, Recipe, Recipe_Ingredient
from .serializers import IngredientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getIngredient(response, id):
    ls = Ingredient.objects.get(id = id)
    return HttpResponse("%s" %ls.name)

@api_view(['GET'])
def getIngredients(response):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
def postIngredient(request):
    print(request.data)
    serializer = IngredientSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)
    return Response(serializer.errors, status = 400)

@api_view(['DELETE'])
def deleteIngredient(request):
    try:
        instance = Ingredient.objects.get(id = request.data.get("id"))
        instance.delete()
        return Response(status = 200)
    except Ingredient.DoesNotExist:
        return Response(status = 404)


@api_view(['GET'])
def recipe(response, id):
    ls = Recipe.objects.get(id = id)
    return HttpResponse("%s" %ls.name)

@api_view(['GET'])
def recipe_ingredient(response, id):
    ls = Recipe_Ingredient.objects.get(id = id)
    return HttpResponse("%s" %ls.name)