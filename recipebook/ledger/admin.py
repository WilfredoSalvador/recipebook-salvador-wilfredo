from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recipe, RecipeIngredient

class TaskInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]
    model = Recipe
    
# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)