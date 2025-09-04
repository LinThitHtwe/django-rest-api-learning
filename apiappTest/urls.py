from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('update_user/', views.update_blog, name="update_blog"),
    path('create_blog/', views.create_blog, name="create_blog"),
    path('blog_list',views.blog_list , name = "blog list"),
    path('update_blog/<int:pk>/', views.update_blog, name="update blog"),
    path('delete_blog/<int:pk>/', views.delete_blog, name="delete blog")
]