from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')
    target_url = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'target_url', 'timestamp', 'read']

    def get_target_url(self, obj):
        # This is a placeholder. You would implement logic to generate a URL
        # based on the target object's type and ID.
        # For example, if target is a Post, return a URL to that post.
        if obj.target:
            return f'/api/{obj.target._meta.model_name}s/{obj.object_id}/'
        return None
