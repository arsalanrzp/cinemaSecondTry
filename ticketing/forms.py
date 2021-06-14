from django import forms

class ShowTimeSearchForms(forms.Form):
    movie_name = forms.CharField(max_length=100, label='movie name', required=False)
