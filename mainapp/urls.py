from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.loading_view, name='loading'),
   path('home/', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact_view, name='contact'),
   path('blog//<int:pk>/', views.blog_view, name='blog'),
   path('blog-list', views.blog_list_view, name='blog-list'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )