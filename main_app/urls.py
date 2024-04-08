from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about', views.about, name='about'),

  # Model 1 - Art CRUD
  path('art/', views.ArtList.as_view(), name='index'),
  path('art/<int:pk>/', views.ArtDetail.as_view(), name='arts_detail'),
  path('art/create/', views.ArtCreate.as_view(), name='arts_create'),
  path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
  path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),

]