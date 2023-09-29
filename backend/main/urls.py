from django.urls import path

from . import views

urlpatterns = [
    path("ingredient/<int:id>", views.ingredient, name="index"),
    path("ingredients/", views.ingredients, name="index"),
    path("recipe/<int:id>", views.recipe, name="index"),
    path("recipe_ingredient/<int:id>", views.recipe_ingredient, name="index"),
]