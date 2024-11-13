from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import AdvocateSerializer
from .models import Advocate

 
@api_view(['GET'])
def endpoint(request):
  data = ['/advocates','advocates/:username']
  return Response(data)


@api_view(['GET','POST'])
def advocates_list(request):
  if request.method == 'GET':
    # /advocates/?query=dennis
    query = request.GET.get('query')
    if query == None:
      query = '' 

  

    advocates = Advocate.objects.filter(Q(username__contains=query) | Q(bio__icontains=query))
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    advocate = Advocate.objects.create(username=request.data['username'],bio=request.data['bio'])
    advocate.save()
    return redirect('advocates')



class AdvocateDetail(APIView):

  def get_object(self,username):
    try:
      return Advocate.objects.get(username=username)
    except:
      raise JsonResponse('Advocate does not exist!')
    
  def get(self,request,username):
    advocate = self.get_object(username)
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  
  def put(self,request,username):
    advocate = self.get_object(username)
    advocate.username = request.data['username']
    advocate.bio = request.data['bio']
    advocate.save()

    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  
  def delete(self,request,username):
    advocate = self.get_object(username)
    advocate.delete()
    return redirect('advocates')
 
 
# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request,username):
#   advocate = Advocate.objects.get(username=username)

#   if request.method == 'GET':  
#     serializer = AdvocateSerializer(advocate,many=False)
#     return Response(serializer.data)


#   if request.method == 'PUT':
#     advocate.username = request.data['username']
#     advocate.bio = request.data['bio']
#     advocate.save()

#     serializer = AdvocateSerializer(advocate,many=False)
#     return Response(serializer.data)
  
#   if request.method == 'delete':
#     advocate.delete()
#     return redirect('advocates')