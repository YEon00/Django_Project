from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/',views.baord_detail),
    path('list/',views.board_list),
    path('write/',views.board_write)
]


