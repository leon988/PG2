from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'location')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
