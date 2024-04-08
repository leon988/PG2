from django.shortcuts import render, redirect
from django.view.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Art, Style, Medium, Comment

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Model 1: Art
class ArtList(ListView):
    model = Art

class ArtDetail(DetailView):
    model = Art

class ArtCreate(CreateView):
    model = Art
    fields =['title', 'image', 'description', 'price', 'style', 'medium']

class ArtUpdate(UpdateView):
    model = Art
    fields = ['title', 'image', 'description', 'price', 'style', 'medium']

class ArtDelete(DeleteView):
    model = Art
    fields = '__all__'

# Model 2: Style


# let's go team