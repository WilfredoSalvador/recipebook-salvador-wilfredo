"""
Importing forms from Django, and RecipeImage with Recipe models for the forms.
"""
from django import forms
from .models import RecipeImage, Recipe


class RecipeForm(forms.ModelForm) :
    """Class for the RecipeForm form."""
    class Meta:
        """Meta class for the fields utilized by RecipeForm."""
        model = Recipe
        fields = "__all__"


class RecipeImageForm(forms.ModelForm) :
    """Class for the RecipeImageForm form."""
    class Meta:
        """Meta class for the fields utilized by RecipeImageForm."""
        model = RecipeImage
        fields = ['image', 'description']
