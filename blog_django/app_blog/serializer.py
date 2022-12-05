from rest_framework import serializers
from .models import TextComment

class TextCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextComment
        fields = '__all__'