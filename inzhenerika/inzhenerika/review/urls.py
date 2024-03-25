from django.urls import path
from . import views

urlpatterns = [
    path('feedback.html', views.ReviewView.as_view())
]