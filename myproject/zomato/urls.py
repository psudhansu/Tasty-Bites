from django.urls import path
from . import views

urlpatterns = [
    # path('',views.welcome,name="welcome"),
    # path('dishes/', views.dish_list, name='dish_list'),
    # path('add_dish/', views.add_dish, name='add_dish'),
    # path('edit_dish/<int:dish_id>/', views.edit_dish, name='edit_dish'),
    # path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('', views.dish_list, name='dish_list'),
    path('add/', views.add_dish, name='add_dish'),
    path('edit/<int:pk>/', views.edit_dish, name='edit_dish'),
    path('delete/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('order_list/', views.order_list, name='order_list'),
    path('take_order/', views.take_order, name='take_order'),
    path('update_order_status/<int:pk>/', views.update_order_status, name='update_order_status'),
    path('order_delete/<int:pk>/', views.order_delete, name='order_delete'),
]