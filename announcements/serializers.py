from rest_framework import serializers

from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    """
    Serializer for the Announcement model ['title', 'price', 'description', 'author', 'created_at']
    """
    class Meta:
        model = Announcement
        fields = '__all__'
