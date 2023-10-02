from django.urls import path
from . import views

urlpatterns = [
    path("ingredient/<int:id>", views.getIngredient, name="getIngredient"),
    path("ingredients/", views.getIngredients, name="getIngredients"),
    path("ingredient/post/", views.postIngredient, name="postIngredient"),
    path("recipe/<int:id>", views.recipe, name="getRecipe"),
    path("recipe_ingredient/<int:id>", views.recipe_ingredient, name="getRecipe_ingredient"),
]