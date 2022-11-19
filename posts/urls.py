from django.urls import path
from .views import (
        PostListView, 
        PostDetailView,
        PostCreateView,
        PostHomeView,
        PostAboutView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('home/', PostHomeView.as_view(), name='home'),
    path('about/', PostAboutView.as_view(), name='about'),
]