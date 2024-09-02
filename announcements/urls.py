from django.urls import path

from .apps import AnnouncementsConfig
from .views import AnnouncementCreateView, AnnouncementListView, AnnouncementUpdateView, AnnouncementDeleteView, \
    AnnouncementDetailView, CommentCreateView, CommentListView, CommentDetailView, CommentUpdateView, CommentDeleteView

app_name = AnnouncementsConfig.name

urlpatterns = [
    path('ad_create/', AnnouncementCreateView.as_view(), name='create'),
    path('', AnnouncementListView.as_view(), name='list'),
    path('ad_view/<int:pk>/', AnnouncementDetailView.as_view(), name='view'),
    path('ad_edit/<int:pk>/', AnnouncementUpdateView.as_view(), name='edit'),
    path('ad_delete/<int:pk>/', AnnouncementDeleteView.as_view(), name='delete'),

    path('comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments', CommentListView.as_view(), name='comment_list'),
    path('comment_view/<int:pk>/', CommentDetailView.as_view(), name='comment_view'),
    path('comment_edit/<int:pk>/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment_delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]