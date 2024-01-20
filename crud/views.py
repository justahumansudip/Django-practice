from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers,TeacherSerializers
from .models import Student,Teacher
# Create your views here.
class StudentView:
    @api_view(['POST'])
    def post_student(request):
       try:
         request_data = request.data
         serializer =StudentSerializers(data=request_data,many=False)
         if serializer.is_valid():
             serializer.save()
             return Response({'message':"student added successfuily"})
       except Exception as e:
           
          return Response({"err":str(e)})

class TeacherView:
    @api_view(['POST'])
    def post_teacher(request):
       try:
         request_data = request.data
         serializer =TeacherSerializers(data=request_data,many=False)
         if serializer.is_valid():
             serializer.save()
             return Response({'message':"Teacher added successfuily"})
       except Exception as e:
           
          return Response({"err":str(e)})    
        
        
@api_view(['GET'])
def getStudent(request):
    students =Student.objects.all()
    serialized_data = StudentSerializers(students,many=True)
    return Response(serialized_data.data)         
            
@api_view(['GET'])
def getTeacher(request):
  try:
    teachers =Teacher.objects.all()
    serialized_data=TeacherSerializers(teachers,many=True)
    return Response(serialized_data.data)
  except Exception as e:
    return Response("ERROR!!",e)


@api_view(['POST'])
def UpdateStudent(request,id):
  try:
    student = Student.objects.get(id=id)
    serialized_data =StudentSerializers(student,data=request.data,many=False,partial=True)
    if serialized_data.is_valid(raise_exception =True):
      serialized_data.save()
      data=serialized_data.data
    return Response({"Message updated successfully ":data})
  except Exception as e:
    return Response("Error!!",e) 
  
@api_view(['POST'])
def UpdateTeacher(request,id):
  try:
    student = Teacher.objects.get(id=id)
    serialized_data =StudentSerializers(student,data=request.data,many=False,partial=True)
    if serialized_data.is_valid(raise_exception =True):
      serialized_data.save()
      data=serialized_data.data
    return Response({"Message updated successfully ":data})
  except Exception as e:
    return Response("Error!!!",e)
  
@api_view(['GET'])
def DeleteStudent(request,id):
  student = Student.objects.get(id=id)
  student.delete()
  return Response({"message":"Student Data Deleted"})  