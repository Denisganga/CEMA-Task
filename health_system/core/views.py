from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import HealthProgram
from .serializers import HealthProgramSerializer

@api_view(['POST'])
def add_program(request):
    serializer = HealthProgramSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_programs(request):
    programs = HealthProgram.objects.all()
    serializer = HealthProgramSerializer(programs, many=True)
    return Response(serializer.data)
