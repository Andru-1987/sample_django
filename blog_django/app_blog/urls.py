# importar los paths para conectar esta app con el main blog_django con las apps

from django.urls import path
from .views import landing_page
from rest_framework import routers
from .viewsets import TextCommentViewSet
from .views import forms

router = routers.SimpleRouter() 
router.register('comment',TextCommentViewSet)

# urlpatterns = [
#     path('', landing_page, name = 'landing_page'),
# ]

urlpatterns = router.urls

urlpatterns += [path('formulario/', forms, name="forms")]