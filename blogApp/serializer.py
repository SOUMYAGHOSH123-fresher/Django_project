from rest_framework import serializers
# from rest_framework.
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'name', 'image', 'desc', 'short_description']
        read_only_fields=['author']
    
    def get_short_description(self, obj):
        return obj.desc[:10]

