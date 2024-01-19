from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers
# Create your views here.
class StudentView:
    @api_view(['POST'])
    def post_student(request):
       try:
         reuest_data = request.data
         serializer =StudentSerializers(data=request_data,many=False)
         if serializer.is_valid():
             serializer.save()
             return Response({'message':"student added successfuily"})
       except Exception as e:
           
          return Response({"err":str(e)})