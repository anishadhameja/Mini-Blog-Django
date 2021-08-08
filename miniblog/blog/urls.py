from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('updatepost/<int:id>', views.update_post, name="update"),
    path('addpost/', views.add_post, name="add"),
    path('delete/<int:id>', views.delete_post, name="delete"),
]
