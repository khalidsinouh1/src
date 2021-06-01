from django.urls import path
from . import views
urlpatterns = [
    path('', views.h1),
    path('scrap', views.scrap, name='scarp')
]
