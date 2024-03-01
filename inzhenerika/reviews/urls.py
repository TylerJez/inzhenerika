from django.urls import path
from reviews.views import ReviewGetView, ReviewCreateView, ReviewDeleteView, ReviewUpdateView, ReviewListView

urlpatterns = [
    path('reviews/get/<int:pk>', ReviewGetView.as_view(), name='get_review'),
    path('reviews/create', ReviewCreateView.as_view(), name='create_review'),
    path('reviews/list', ReviewListView.as_view(), name='list_review'),
    path('reviews/delete/<int:pk>', ReviewDeleteView.as_view(), name='delete_review'),
    path('reviews/update/<int:pk>', ReviewUpdateView.as_view(), name='update_review'),
]
