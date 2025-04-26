from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import HealthProgram,Enrollment,Client
from .serializers import HealthProgramSerializer,ClientSerializer,EnrollmentSerializer

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

@api_view(['POST'])
def register_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def enroll_client(request):
    client_id = request.data.get('client')
    program_id = request.data.get('program')

    if not client_id or not program_id:
        return Response({'error': 'Client and Program are required.'}, status=400)

    try:
        client = Client.objects.get(id=client_id)
        program = HealthProgram.objects.get(id=program_id)

        enrollment = Enrollment.objects.create(client=client, program=program)

        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=201)

    except Client.DoesNotExist:
        return Response({'error': 'Client not found.'}, status=404)
    except HealthProgram.DoesNotExist:
        return Response({'error': 'Program not found.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def list_enrollments(request):
    enrollments = Enrollment.objects.select_related('client', 'program').all()
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)