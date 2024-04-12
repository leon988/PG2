from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comment, Art, Medium, Style


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'location']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'image', 'date', 'price', 'style', 'medium','description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'image': forms.TextInput(attrs={'placeholder': 'Enter a direct image URL of your art.'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select creation date'}),
            'price': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'Enter Valuation'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medium'].queryset = Medium.objects.all()
        self.fields['style'].queryset = Style.objects.all()


# https://ccbv.co.uk/
# __init__ method of class ArtForm is used to customize the queryset for medium and style.
# this makes all available options from the Medium and Style models, respectively