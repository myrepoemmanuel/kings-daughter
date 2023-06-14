from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', views.register, name="site-reg"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name="site-profile"),
    path('changePassword', views.change_password, name='change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="site-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name="site-logout"),
]