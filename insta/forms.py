from django import forms

class Trial(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=200)