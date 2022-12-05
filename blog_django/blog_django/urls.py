from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include

from app_blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_blog.urls')),
    # re_path(r'^hola.*\/$', views.test_page , name='test') #utilizando un pattern de regexp
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
