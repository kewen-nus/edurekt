from rest_framework import serializers

from modules.models import Module


class ModuleSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    lecturers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ('code', 'name', 'description', 'time', 'room', 'students', 'lecturers')
