from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
class StudentListCreateAPI(generics.ListCreateAPIView):
    queryset=Student.objects.all().order_by('id')
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
