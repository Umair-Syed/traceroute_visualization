from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('getgraph/', views.graph_view, name='graph'),
    path('getmap/', views.map_view, name='map'),
]