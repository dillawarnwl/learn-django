from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('single-post/<int:pk>/', views.blog_detail, name='single-post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]
