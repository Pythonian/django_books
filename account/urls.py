from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('login/',
         auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('library/', views.library, name='library'),
    path('settings/', views.settings, name='settings'),
    path('stories/', views.stories, name='user_stories'),
]
