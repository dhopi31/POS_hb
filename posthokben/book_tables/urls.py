from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book-use-raw/', views.use_raw, name='use_raw'),
    path('book-pay/', views.pay_type, name='pay_type'),
    path('search/', views.search, name='search'),
    path('search_use_raw/', views.search_use_raw, name='search_use_raw'),
    path('search_pay/', views.search_pay, name='search_pay'),
]