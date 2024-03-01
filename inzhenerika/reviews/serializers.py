from rest_framework.serializers import ModelSerializer
from reviews.models import ReviewModel


class ReviewModelSerializer(ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'
