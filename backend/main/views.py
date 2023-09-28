from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredient, Recipe, Recipe_Ingredient
# Create your views here.
def ingredient(response, id):
    ls = Ingredient.objects.get(id=id)
    return HttpResponse("%s" %ls.name)
def recipe(response, id):
    ls = Recipe.objects.get(id=id)
    return HttpResponse("%s" %ls.name)
def recipe_ingredient(response, id):
    ls = Recipe_Ingredient.objects.get(id=id)
    return HttpResponse("%s" %ls.name)