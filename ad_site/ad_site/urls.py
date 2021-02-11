import os
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.static import serve


urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('hello/', include('hello.urls')),
    path('polls/', include('polls.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Serve the favicon
urlpatterns += [
    path(
        'favicon.ico',
        serve,
        {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(
        0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
