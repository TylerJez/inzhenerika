from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review, name='review'),
    path('notify_review/', views.notify_review, name='notify_review'),
    #path('feedback.html', views.ReviewView.as_view()),
]