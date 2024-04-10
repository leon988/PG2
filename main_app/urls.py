from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # Model 1 - Art CRUD
  path('art/', views.ArtList.as_view(), name='index'),
  path('art/<int:pk>/', views.ArtDetail.as_view(), name='arts_detail'),
  path('art/create/', views.ArtCreate.as_view(), name='arts_create'),
  path('art/<int:pk>/update/', views.ArtUpdate.as_view(), name='arts_update'),
  path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name='arts_delete'),

  # Model 2 - Style RUD
  path('style/', views.StyleList.as_view(), name='styles_index'),
  path('style/<int:pk>/', views.StyleDetail.as_view(), name='styles_detail'),
  path('style/<int:pk>/update/', views.StyleUpdate.as_view(), name='styles_update'),
  path('style/<int:pk>/delete/', views.StyleDelete.as_view(), name='styles_delete'),

  # Model 3 - Medium RUD
  path('medium/', views.MediumList.as_view(), name='mediums_index'),
  path('medium/<int:pk>/', views.MediumDetail.as_view(), name='mediums_detail'),
  path('medium/<int:pk>/update/', views.MediumUpdate.as_view(), name='mediums_update'),
  path('medium/<int:pk>/delete/', views.MediumDelete.as_view(), name='mediums_delete'),

  # Model 4 - Comment CRUD
  path('comment/', views.CommentList.as_view(), name='comments_index'),
  path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comments_detail'),
  path('comment/create/', views.CommentCreate.as_view(), name='comments_create'),
  path('art/<int:pk>/comment/create/', views.CommentCreate.as_view(), name='comments_create'),
  path('comment/<int:pk>/comment/update/', views.CommentUpdate.as_view(), name='comments_update'),
  path('comment/<int:pk>/comment/delete/', views.CommentDelete.as_view(), name='comments_delete'),

  # Model 5 - User
  path('accounts/signup/', views.signup, name='signup'),


# hi team!
]