from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'blog', views.blog_post, name='view_blog'),
    path(r'ajax/quote', views.quote, name='quote'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)