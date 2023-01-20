from django.urls import path

from count import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('count/', views.CountView.as_view(), name='count'),
]