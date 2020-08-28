from rest_framework import serializers

# Internal Imports
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = (
            'content'
        )