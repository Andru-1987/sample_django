from rest_framework import viewsets
from .serializer import TextCommentSerializer
from .models import TextComment

class TextCommentViewSet(viewsets.ModelViewSet):
    queryset = TextComment.objects.all()
    serializer_class = TextCommentSerializer