from django import forms 
from .models import Posts


class Postform(forms.MeodelForm):
    class Meta:
        model = Posts
        fields = '__all__'