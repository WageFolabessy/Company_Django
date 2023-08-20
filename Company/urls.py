from django.urls import path
from .views import IndexView, CreateOrStoreView, DetailView, EditOrUpdateView, DeleteView

app_name = 'company'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateOrStoreView.as_view(), name='store'),
    path('<str:name>/', DetailView.as_view(), name='detail'),
    path('<str:name>/edit/', EditOrUpdateView.as_view(), name='update'),
    path('<str:name>/delete/', DeleteView.as_view(), name='delete'),
]

