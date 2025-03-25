"""Module importing the admin panels"""

from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, RecipeImage

class RecipeInLine(admin.TabularInline):
    """Class representing an Inline Admin"""

    model = RecipeIngredient

class RecipeImageInLine(admin.TabularInline):
    """Class representing an Inline for the Recipe images."""
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Recipe model"""

    model = Recipe
    inlines = [RecipeInLine, RecipeImageInLine]


class IngredientAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Ingredient model"""
    model = Ingredient
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
