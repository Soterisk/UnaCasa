from django.urls import path
from UserApp import views

urlpatterns = [
    # other urls
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    # other urls
]