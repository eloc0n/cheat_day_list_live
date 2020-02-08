from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_list/<str:pk>', views.updateList, name='update_list'),
    path('delete/<str:pk>', views.deleteList, name='delete'),
]