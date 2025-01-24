from django.urls import path
from .views import UserListView, UserDetailView, RegisterUserView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('register/', RegisterUserView.as_view(), name='user_register'),
]
