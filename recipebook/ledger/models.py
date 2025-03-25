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

class Recipe(models.Model):
    """Class representing a recipe in the recipe book."""

    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author',)
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
        """Function returning date recipe was last updated."""
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

class RecipeImage(models.Model):
    """Class to create """
    image = models.ImageField(upload_to="images/", default=None)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        related_name='recipe',)
