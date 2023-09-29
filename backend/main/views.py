from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Ingredient, Recipe, Recipe_Ingredient
import json

# Create your views here.
def ingredient(response, id):
    ls = Ingredient.objects.get(id=id)
    return HttpResponse("%s" %ls.name)

def ingredients(response):
    ls = Ingredient.objects.all()
    data = [{'id': item.id, 'name': item.name} for item in ls]
    return JsonResponse(data, safe=False)

def recipe(response, id):
    ls = Recipe.objects.get(id=id)
    return HttpResponse("%s" %ls.name)
def recipe_ingredient(response, id):
    ls = Recipe_Ingredient.objects.get(id=id)
    return HttpResponse("%s" %ls.name)