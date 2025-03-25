"""
Modules importing django views, HttpResponse and Recipe for url views.
This also includes RecipeImage, LoginRequiredMixin, login_required for the 
function based views
"""
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeList(ListView):
    """Class viewing the list of recipes."""
    model = Recipe
    template_name = "recipes/list.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    """Class creating a new recipe."""
    model = Recipe
    template_name = "recipe/add.html"
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-list')
    redirect_field_name = "registration/login.html"

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    """Class for recipe details using an UpdateView."""
    model = Recipe
    template_name = "recipe/detail.html"
    form_class = RecipeImageForm
    redirect_field_name = "registration/login.html"

@login_required(redirect_field_name="registration/login.html")
def recipe_image(request, pk):
    """Function used to add images for a recipe."""
    form = RecipeImageForm()
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            i = RecipeImage()
            i.image = form.cleaned_data.get('image')
            i.description = form.cleaned_data.get('description')
            i.recipe = Recipe.objects.get(pk=pk)
            recipe = i.recipe
            i.save()
            return redirect('ledger:recipe-detail', pk=recipe.pk)

    ctx = {"form": form, "recipe":Recipe.objects.get(pk=pk)}
    return render(request, 'recipe/add_image.html', ctx)
