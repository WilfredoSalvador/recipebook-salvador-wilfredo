"""Module importing the admin panels"""

from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeInLine(admin.TabularInline):
    """Class representing an Inline Admin"""

    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Recipe model"""

    inlines = [RecipeInLine,]
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Ingredient model"""
    model = Ingredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
