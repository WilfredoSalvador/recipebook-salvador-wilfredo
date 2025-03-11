"""Modules importing django views, HttpResponse and Recipe for url views."""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeList(ListView):
    """Class viewing the list of recipes."""

    model = Recipe
    template_name = "recipes/list.html"

class RecipeDetail(LoginRequiredMixin, DetailView):
    """Class viewing a recipe in detail."""

    model = Recipe
    template_name = "recipe/detail.html"
    redirect_field_name = "registration/login.html"
