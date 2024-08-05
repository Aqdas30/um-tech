<<<<<<< HEAD
# services/serializers.py

=======
>>>>>>> 137d0f08509a2b46bb25de8a6260b8d467133386
from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image']
=======
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['title', 'description', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
>>>>>>> 137d0f08509a2b46bb25de8a6260b8d467133386
