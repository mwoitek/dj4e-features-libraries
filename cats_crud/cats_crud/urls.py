from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('hello/', include('hello.urls')),
    path('polls/', include('polls.urls')),
]
