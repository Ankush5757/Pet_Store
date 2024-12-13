from django.urls import path
from .views import set_cookie, set_session, display_info

urlpatterns = [
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('set_session/', set_session, name='set_session'),
    path('info/', display_info, name='display_info'),
]
