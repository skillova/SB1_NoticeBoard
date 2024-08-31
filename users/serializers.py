from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model ['email', 'first_name', 'last_name', 'phone', 'email', 'role', 'image']
    """
    class Meta:
        model = User
        fields = '__all__'
