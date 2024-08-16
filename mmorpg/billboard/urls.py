from django.urls import path
from .views import AdCreate, AdsList, AdDetail, AdUpdate, AdDelete, MyResponsesList, response_handle, subscriptions

urlpatterns = [
  path('', AdsList.as_view(), name='ad_list'),
  path('responses/', MyResponsesList.as_view(), name='responses'),
  path('responses/handle', response_handle, name='response_handle'),
  path('<int:id>', AdDetail.as_view(), name='ad_detail'),
  path('create/', AdCreate.as_view(), name='ad_create'),
  path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_edit'),
  path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
  path('subscriptions/', subscriptions, name='subscriptions'),
]