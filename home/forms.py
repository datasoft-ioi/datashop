from django import forms
from home.models import Contact

class SearchForm(forms.Form):

    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()



