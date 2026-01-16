from django.urls import path
from . import views


urlpatterns = [
        path("", views.home, name="home"),
        path("greeting/", views.greeting, name="greeting"),
        path("form/", views.form_view,  name="form"),
        path("success/", views.success_view, name="success"),
        path("data/", views.data, name="data"),
        path("form2/", views.register_view, name="form2"),
        ]
