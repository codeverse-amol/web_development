from demoApp.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def StudentsAPIView(request):
    
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        print("Data retrieved")
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Data Saved")
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)