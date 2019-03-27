from django import forms
from .models import Profile,Image,Comments

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []
