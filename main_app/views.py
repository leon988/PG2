from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ArtCreate(LoginRequiredMixin, CreateView):
    model = Art
    fields =['title', 'image', 'description', 'price', 'style', 'medium']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArtUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    fields = ['title', 'image', 'description', 'price', 'style', 'medium']

class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url= '/art'

# Model 2: Style
class StyleList(ListView):
    model = Style

class StyleDetail(LoginRequiredMixin, DetailView):
    model = Style

class StyleUpdate(LoginRequiredMixin, UpdateView):
    model = Style
    fields = '__all__'

class StyleDelete(LoginRequiredMixin, DeleteView):
    model = Style
    success_url = '/style'

# Model 3: Medium
class MediumList(ListView):
    model = Medium

class MediumDetail(LoginRequiredMixin, DetailView):
    model = Medium

class MediumUpdate(LoginRequiredMixin, UpdateView):
    model = Medium
    fields = '__all__'

class MediumDelete(LoginRequiredMixin, DeleteView):
    model = Medium
    success_url = '/medium'

# Model 4: Comment
class CommentList(ListView):
    model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = '__all__'

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = '__all__'

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/comment'

# SIGNUP
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)