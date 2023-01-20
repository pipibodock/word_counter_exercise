from django.urls import path

from count import views

urlpatterns = [
    path('', views.index, name='count'),
]