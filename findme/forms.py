from django import forms
from .models import ItemLost


class Lost(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=100)
    image = forms.ImageField()

    class Meta:
        model = ItemLost
        fields = ['title', 'description', 'location', 'image', 'found']


