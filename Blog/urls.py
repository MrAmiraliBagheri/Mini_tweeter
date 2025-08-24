from django.urls import path
from . import views

urlpatterns = [
    path('', views.TweetList, name='tweet_list'),
    path('create/', views.CreatTweet, name='tweet_create'),
    path('edit/<int:pk>/', views.EditTweet, name='tweet_edit'),
    path('delete/<int:pk>/', views.DelTweet, name='tweet_delete'),
    path('signup/', views.SignUpView, name='register'),
    path('login/', views.login_view, name='login'),
]
