from django.urls import path, re_path
from app_pages import views

app_name = "app_pages"

urlpatterns = [
    # Dynamic urls view
    re_path(r'^$', views.index, name='index'),
    # Streamlit proxy - should be after all main path's 
    path('streamlit/', views.streamlit_proxy, name='streamlit-proxy'),
    re_path(r'^streamlit/(?P<path>.*)$', views.streamlit_proxy),
]