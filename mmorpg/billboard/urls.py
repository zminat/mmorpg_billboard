from django.urls import path
from .views import AdCreate, AdsList, AdDetail, AdUpdate, AdDelete

urlpatterns = [
  path('ads/', AdsList.as_view(), name='ad_list'),
  path('ads/<int:id>', AdDetail.as_view(), name='ad_detail'),
  path('ads/create/', AdCreate.as_view(), name='ad_create'),
  path('ads/<int:pk>/edit/', AdUpdate.as_view(), name='ad_edit'),
  path('ads/<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
]