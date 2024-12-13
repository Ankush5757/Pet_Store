from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_pic/<int:id>/', views.profile_pic, name='profile_pic'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
]


