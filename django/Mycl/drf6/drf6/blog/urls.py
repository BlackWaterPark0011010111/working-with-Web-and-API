from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view()),
    path("posts/<int:pk>", views.PostRetrieveUpdateDestroyView.as_view()),
    path("tags/", views.TagListCreateView.as_view()),
    path("tags/<int:pk>", views.TagRetrieveUpdateDestroyView.as_view()),
]
