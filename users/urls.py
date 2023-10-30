from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout.as_view(), name='logout'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('', views.signup.as_view(), name='main')
]
