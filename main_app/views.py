from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Art, Style, Medium, Comment, Profile
from .forms import UserForm, ProfileForm, CommentForm, ArtForm


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
    form_class = ArtForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# super() function is used to refer to the parent class 
# it allows you to call methods defined in the superclass/parent from the subclass enables you to extend and customize the functionality inherited from the parent class.
# This ensures that the user field of the Art model is populated with the current user before saving the form.

class ArtUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    form_class = ArtForm

class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url= '/art'

@login_required
def increment_likes(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    art.like += 1
    art.save()
    return redirect('arts_detail', pk=art_id)
# Django shortcut function used to retrieve an object, but if not found, 404 error
# Error handling, checks if Art object with the PK exists in the database before proceeding

# Model 2: Style
class StyleList(ListView):
    model = Style

class StyleDetail(DetailView):
    model = Style
    template_name = 'main_app/style_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        style = self.get_object()
        context['artworks'] = Art.objects.filter(style=style)  
        return context
#  provide additional data to the template context beyond default, so we can access artworks in template

# class StyleUpdate(LoginRequiredMixin, UpdateView):
#     model = Style
#     fields = '__all__'

# class StyleDelete(LoginRequiredMixin, DeleteView):
#     model = Style
#     success_url = '/style'


# Model 3: Medium
class MediumList(ListView):
    model = Medium

class MediumDetail(DetailView):
    model = Medium
    template_name = 'main_app/medium_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medium = self.get_object()
        context['artworks'] = Art.objects.filter(medium=medium)  
        return context

# class MediumUpdate(LoginRequiredMixin, UpdateView):
#     model = Medium
#     fields = '__all__'

# class MediumDelete(LoginRequiredMixin, DeleteView):
#     model = Medium
#     success_url = '/medium'


# Model 4: Comment
# class CommentList(ListView):
#     model = Comment

# class CommentDetail(DetailView):
#     model = Comment

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/art_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.art = get_object_or_404(Art, pk=self.kwargs['pk'])  # Associate the comment with the relevant art
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['art'] = get_object_or_404(Art, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('arts_detail', args=[self.object.art.pk])

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main_app/comment_form.html'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('arts_detail', kwargs={'pk': self.object.art.pk})

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('arts_detail', kwargs={'pk': self.object.art.pk})
# reverse_lazy is a Django function similar to reverse, but it evaluates at a later time when it's needed
# After deleting the comment the user will be redirected to the detail view where deleted comment belonged.


# Django Authentication - Sign Up
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# Model 5: Profile
@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile/profile_detail.html', {'user': user})

@login_required
def profile(request):
    error_message = ''
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_detail')
        else:
            error_message = 'Invalid form submission - please try again'
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    context = {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'profile/profile_form.html', context)



# -----
# ref: Class Based Views -- https://ccbv.co.uk/
# ref: get_object_or_404 -- https://www.sankalpcjonna.com/learn-django/use-get-object-or-404-in-django-to-write-lesser-code
# ref: https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
# ref: super() -- https://www.geeksforgeeks.org/python-super/#
# ref: reverse_lazy() -- https://forum.djangoproject.com/t/understanding-reverse-and-reverse-lazy/22951
# ref: adding extra context -- https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/