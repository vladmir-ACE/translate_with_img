from django.urls import path
from .views import TranslateCreateView, TranslateListView,translate_delete

urlpatterns = [
    path('create/', TranslateCreateView.as_view(), name='translate_create'),
    path('', TranslateListView.as_view(), name='translate_list'),
    path('delete/<int:pk>/', translate_delete, name='translate_delete'),
]
