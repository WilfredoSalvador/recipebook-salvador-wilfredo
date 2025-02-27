from django.urls import path
from .views import index, recipe_list, recipe_detail
urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_list.as_view(), name= 'recipe-list'),
    path('recipe/<int:pk>', recipe_detail.as_view(), name = "recipe-detail"),
    ]

app_name = "ledger"