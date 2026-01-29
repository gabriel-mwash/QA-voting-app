from django.urls import path
from . import views


urlpatterns = [
        path("", views.home, name="home"),
        path("success/", views.success_view, name="success"),
        path("questions/", views.submittedQuestions, name="questions"),
        ]
