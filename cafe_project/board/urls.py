from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.board_read, name ='board_read'),
    path('read/<int:pk>', views.board_read_one, name='board_read_one'),
    path('create/', views.board_create, name='board_create'),
    path('pre_update/<int:pk>', views.pre_update, name = 'pre_update'),
    path('update/<int:pk>', views.board_update, name = 'update'),
    path('delete/<int:pk>', views.board_delete, name = 'delete'),
]