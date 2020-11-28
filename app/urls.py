from django.urls import path
from . import views

urlpatterns = (
    path('', views.homepage, name='homepage'),
    path('estimates/', views.estimates, name='estimates'),
    path('estimates/layout_ugd_city/', views.layout_ugd_city, name='layout_ugd_city'),
)