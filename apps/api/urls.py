from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView, APIFrontendView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
    path('ui/items/', APIFrontendView.as_view(), name='api-item-ui'),
]