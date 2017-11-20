from django import forms

class LocationForm(forms.Form):
    name = forms.CharField(max_length=50)
    num_restaurants = forms.IntegerField()
    predators = forms.CharField(max_length=100)
    img_url = forms.CharField(max_length=200)

