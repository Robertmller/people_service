from django.urls import path

from core import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name="index")
]
