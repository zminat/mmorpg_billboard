from django.urls import path
from .views import AdCreate, AdsList, AdDetail, AdUpdate, AdDelete, MyAdsList, MyResponsesList

urlpatterns = [
  path('', AdsList.as_view(), name='ad_list'),
  path('myads/', MyAdsList.as_view(), name='my_ads'),
  path('responses/', MyResponsesList.as_view(), name='responses'),
  path('<int:id>', AdDetail.as_view(), name='ad_detail'),
  path('create/', AdCreate.as_view(), name='ad_create'),
  path('<int:pk>/edit/', AdUpdate.as_view(), name='ad_edit'),
  path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
]