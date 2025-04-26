from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import add_program, get_programs
from . import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/programs/add/', add_program),
    path('api/programs/list/', get_programs),
    path('clients/register/', views.register_client),
    path('clients/enroll/', views.enroll_client),
    path('clients/enrollments/', views.list_enrollments),
    path('clients/list/', views.list_clients, name='list-clients')
]
