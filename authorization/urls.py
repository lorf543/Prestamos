from django.urls import path

from . import views

urlpatterns = [
    path('login_user/',views.login_user, name='login_user'),
    path('register_user/',views.register_user,name='register_user'),
    path('log_out/',views.log_out,name='log_out'),
]