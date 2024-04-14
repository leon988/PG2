from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comment, Art, Medium, Style


# Model 1 - Profile
class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'image', 'date', 'price', 'style', 'medium','description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'image': forms.TextInput(attrs={'placeholder': 'Enter a direct image URL of your art'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select creation date'}),
            'price': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'Enter Valuation'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medium'].queryset = Medium.objects.all()
        self.fields['style'].queryset = Style.objects.all()
# __init__ method of class ArtForm is used to customize the queryset for medium and style.
# this makes all available options from the Medium and Style models in the form


# Model 4 - Profile
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


# Model 5 - Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'location']


# Django Authentication - Sign Up
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']




# -----
# ref: https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django
