from django.urls import path

from . import views

urlpatterns = [
    path('', views.register_new_user, name='api')
]