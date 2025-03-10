"""Module providing a base of models for python."""

from django.db import models
from django.urls import reverse
from UserAccounts.models import Profile

class Ingredient(models.Model):
    """Class representing an ingredient in the recipe."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Function returning ingredient name."""
        return self.name

    def get_absolute_url(self):
        """Function returning url of ingredient details."""
        return reverse('ingredient_detail', args=[str(self.pk)])


class Recipe(models.Model):
    """Class representing a recipe in the recipe book."""

    Author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='Author',)
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        """Function returning recipe name."""
        return self.name
    
    def get_created(self):
        """Function returning date recipe was created."""
        return self.created_on
    
    def get_updated(self):
        """fFunction returning date recipe was last updated."""
        return self.updated_on

    def get_absolute_url(self):
        """Function returning url of recipe details."""
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    """Class creating foreign keys for ingredient, recipe, and string for quantity. """

    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey( 
        Ingredient, on_delete=models.SET_NULL, null=True,
        related_name='recipe',)

    recipe = models.ForeignKey(
        Recipe, on_delete=models.SET_NULL, null=True,
        related_name='ingredients',)
