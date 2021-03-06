from django.urls import path
from . import views


app_name = 'cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
]
