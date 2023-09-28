from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class Recipe_Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=300)

    def __str__(self):
        return self.recipe_id