from rest_framework import generics
from reviews.models import ReviewModel
from reviews.serializers import ReviewModelSerializer


class ReviewGetView(generics.RetrieveAPIView):
    queryset = ReviewModel
    serializer_class = ReviewModelSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = ReviewModel
    serializer_class = ReviewModelSerializer


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = ReviewModel
    serializer_class = ReviewModelSerializer


class ReviewListView(generics.ListAPIView):
    queryset = ReviewModel
    serializer_class = ReviewModelSerializer


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = ReviewModel
    serializer_class = ReviewModelSerializer
