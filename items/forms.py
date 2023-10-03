from django import forms
from .models import items

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border border-gray-700  mb-10"
class itemForm(forms.ModelForm):
    class Meta:
        model = items
        fields= ("name","description","price","image","itemCategory")

        widgets = {
            'itemCategory' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'price' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }) 
        }
class editForm(forms.ModelForm):
    class Meta:
        model = items
        fields= ("isSold","name","description","price","image")

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            }) ,
            'price' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }) ,
        }