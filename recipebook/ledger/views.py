from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
def index(request):
    return HttpResponse('Check http://localhost:8000/recipes/list for the Recipe Book.')
# Create your views here.

# def recipe_list(request):
#     recipes = Recipe.recipes.all()
#     ctx = {
    
#     "recipes" : recipes
#     #"recipes": [
#         #{
#         #    "name": "Recipe 1",
#         #    "link": "/recipe/1"
#        # },
#         #{
#        #     "name": "Recipe 2",
#       #      "link": "/recipe/2"
#      #   }
#     #]
#     }
#     return render(request, 'recipes/list.html', ctx)

class recipe_list(ListView):
    model = Recipe
    template_name = "recipes/list.html"

class recipe_detail(DetailView):
    model = Recipe
    template_name = "recipe/detail.html"
# # def recipe_1(request):

#     ctx = {
#     Ingredients = Ingredient.ingredients.filter(recipe__recipe__name="Recipe 1")


#     "ingredients" : ingredients
#     # "name": "Recipe 1",
#     #"ingredients": [
#      #   {
#       #      "name": "tomato",
#        #     "quantity": "3pcs"
#         #},
#         #{
#     #        "name": "onion",
#      #       "quantity": "1pc"
#       #  },
#        # {
#       #      "name": "pork",
#        #     "quantity": "1kg"
#        # },
#        # {
#        #     "name": "water",
#         #    "quantity": "1L"
#      #   },
#       #  {
#       #      "name": "sinigang mix",
#       #      "quantity": "1 packet"
#        # }
#     #],
#     #"link": "/recipe/1"
# }
#     return render(request, 'recipe/1.html', ctx)

# # # def recipe_2(request):
#     ctx = {
#     "name": "Recipe 2",
#     "ingredients": [
#         {
#             "name": "garlic",
#             "quantity": "1 head"
#         },
#         {
#             "name": "onion",
#             "quantity": "1pc"
#         },
#         {
#             "name": "vinegar",
#             "quantity": "1/2cup"
#         },
#         {
#             "name": "water",
#             "quantity": "1 cup"
#         },
#         {
#             "name": "salt",
#             "quantity": "1 tablespoon"
#         },
#         {
#             "name": "whole black peppers",
#             "quantity": "1 tablespoon"
#         },
#         {
#             "name": "pork",
#             "quantity": "1 kilo"
#         }
#     ],
#     "link": "/recipe/2"
# }
#     return render(request, 'recipe/2.html', ctx)