from django.urls import path
from .views import (
    ListCreateAPIView, 
    CheckListAPIView,
    ItemCreateAPIView,
    ListItemAPIView,
    )

urlpatterns = [
    path('', ListCreateAPIView.as_view()), #create

    path('list/<int:pk>/', CheckListAPIView.as_view()), #RUD operations
    
    path('createItem/', ItemCreateAPIView.as_view()),
    
    path('item/<int:pk>/', ListItemAPIView.as_view()),
    
]    