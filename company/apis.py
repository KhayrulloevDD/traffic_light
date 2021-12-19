from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, JuristicPerson, Department
from .serializers import UserSerializer, JuristicPersonSerializer, DepartmentSerializer


@api_view(['GET'])
def get_all(request):
    juristic_persons = JuristicPerson.objects.all()
    serializer = JuristicPersonSerializer(juristic_persons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
