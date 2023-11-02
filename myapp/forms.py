from django import forms
from .models import Food

class ItemForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','carbs','protein','fats','calories']