"""Module providing a function redirecting urls to recipe book."""

from django.urls import path
from .views import RecipeList, RecipeDetail
urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name= 'recipe-list'),
    path('recipe/<int:pk>', RecipeDetail.as_view(), name = "recipe-detail"),
    ]

app_name = "ledger"
