from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'authenticationApp'


urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('register/', views.registerPage, name='registerPage'),
    path('accounts/profile/', views.profilePage, name='profilePage'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),

]
