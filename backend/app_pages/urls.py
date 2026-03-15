from django.urls import re_path
from app_pages import views

app_name = "app_pages"

urlpatterns = [
    # Dynamic urls view
    re_path(r'^$', views.index, name='index'),
]