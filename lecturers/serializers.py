from rest_framework import serializers

from lecturers.models import Lecturer


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'name', 'department', 'module')
