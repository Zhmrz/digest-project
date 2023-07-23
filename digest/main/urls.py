from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('get_digest/', views.get_digest, name='get_digest')
]