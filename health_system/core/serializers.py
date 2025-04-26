from rest_framework import serializers
from .models import HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = '__all__'
from rest_framework import serializers
from .models import Client, Enrollment, HealthProgram

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    program_name = serializers.CharField(source='program.name', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'client', 'program_name', 'date_enrolled']
