"""Module providing a function redirecting urls to recipe book."""

from django.urls import path
from .views import recipe_image, RecipeList, RecipeCreateView ,RecipeUpdateView
urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name= 'recipe-list'),
    path('recipe/<int:pk>', RecipeUpdateView.as_view(), name = "recipe-detail"),
    path('recipe/add', RecipeCreateView.as_view(), name='add'),
    path('recipe/<int:pk>/add_image', recipe_image, name='add-image')
    ]

app_name = "ledger"
