"""docs/url.py"""
from django.urls import path

from .views import serve_docs, serve_index

urlpatterns = [
    path('', serve_index),
    path('<path>', serve_docs),
]
