from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsDoctor])
def doctor_dashboard_api(request):
    return Response({"message": "Welcome, Doctor!"})
