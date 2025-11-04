from django.urls import path
from .views import ItemViewSet, ItemFrontendView

item_list = ItemViewSet.as_view({'get': 'list', 'post': 'create'})
item_detail = ItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('items/', item_list, name='item-list-create'),
    path('items/<int:pk>/', item_detail, name='item-detail'),
    # frontend UI
    path('ui/items/', ItemFrontendView.as_view(), name='item-ui'),
]