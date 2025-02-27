"""Module importing the admin panels"""

from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeInLine(admin.TabularInline):
    """Class representing an Inline Admin"""

    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    """Class for the Admin panel of Recipe model"""

    inlines = [RecipeInLine,]
    model = Recipe

admin.site.register(Recipe, RecipeAdmin)
