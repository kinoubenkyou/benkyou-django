from django.urls import path

from main.views import UserListView, UserDetailView, UserCreateView, UserUpdateView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]
