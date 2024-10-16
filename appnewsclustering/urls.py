# company_info/urls.py
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('company/<int:company_id>/', home, name='company_home'),
]
