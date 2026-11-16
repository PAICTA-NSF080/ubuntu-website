from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request/new/', views.create_request, name='create_request'),
    path('request/<int:pk>/update/', views.update_request, name='update_request'),
    path('opportunity/new/', views.create_opportunity, name='create_opportunity'),
    path('opportunity/<int:pk>/apply/', views.apply_opportunity, name='apply_opportunity'),
    path('application/<int:pk>/review/', views.review_application, name='review_application'),
    path('', views.register, name='home'),
]