from django.urls import path
# from django.views.generic import TemplateView
from . import views


app_name = 'autos'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
]
