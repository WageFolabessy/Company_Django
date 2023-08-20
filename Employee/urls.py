from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_or_store, name='store'),
    path('detail/<str:id>/', views.detail, name='detail'),
    path('edit/<str:id>/', views.edit_or_update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
]
