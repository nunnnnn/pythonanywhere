from django.forms import ModelForm
from django import forms

from .models import Vegetable,Farm

class addFarm(ModelForm):
    class Meta:
        model = Farm
        fields = ['Farm_Name']


class addVegetable(ModelForm):
    class Meta:
        model = Vegetable
        fields = ['Vegetable_Name','Price','Season','FarmName']


searchchoices = (
        (1 , 'ชื่อผัก'),
    )

class SearchForm(forms.Form):
    

    SearchBy = forms.ChoiceField(choices=searchchoices)
    keyword = forms.CharField(max_length=100)
