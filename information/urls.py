from django.urls import path
from . import views

urlpatterns = [
    path('', views.information),
    path('about/', views.about, name='about-page'),
]