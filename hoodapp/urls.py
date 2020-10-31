from django.urls import path
from django.conf.urls import url
from . import views
from hoodapp.views import (PostDetailView,PostDeleteView)

urlpatterns = [
    path('', views.home, name='hoodapp-home'),
    path('homepage/', views.homepage, name='hoodapp-homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.new_post, name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^search/', views.search_results, name='search_results'),
]