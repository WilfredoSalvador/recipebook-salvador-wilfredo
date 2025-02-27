"""Modules importing django views, HttpResponse and Recipe for url views."""
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

def index(request):
    """function printing homepage message."""
    return HttpResponse('Check http://localhost:8000/recipes/list for the Recipe Book.')

class RecipeList(ListView):
    """Class viewing the list of recipes."""

    model = Recipe
    template_name = "recipes/list.html"

class RecipeDetail(DetailView):
    """Class viewing a recipe in detail."""

    model = Recipe
    template_name = "recipe/detail.html"
