from django.urls import path

from .apps import AnnouncementsConfig
from .views import AnnouncementCreateView, AnnouncementListView, AnnouncementUpdateView, AnnouncementDeleteView, \
    AnnouncementDetailView

app_name = AnnouncementsConfig.name

urlpatterns = [
    path('ad_create/', AnnouncementCreateView.as_view(), name='create'),
    path('', AnnouncementListView.as_view(), name='list'),
    path('ad_view/<int:pk>/', AnnouncementDetailView.as_view(), name='view'),
    path('ad_edit/<int:pk>/', AnnouncementUpdateView.as_view(), name='edit'),
    path('ad_delete/<int:pk>/', AnnouncementDeleteView.as_view(), name='delete'),
]