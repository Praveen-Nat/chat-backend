from django.shortcuts import render
from .serializers import ContactSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Contact



# Create your views here.
@csrf_exempt
@api_view(['POST'])
def contactPost(request):
    print(request.data)
    Contact.objects.create(name=request.data['name'],phone=request.data['phone'],email=request.data['email'],company= request.data['company'])
    return JsonResponse(request.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def contactGet(request):
    print(request.data)
    # contacts = ContactSerializer(Contact.objects.all(), many=True) 
    contact_obj = Contact.objects.all()
    response = {}
    for k in contact_obj:
        response[str(k.id)] = { "Name": k.name, "Phone Number": str(k.phone), "Email": k.email, "Company Name": k.company}
    return Response(response)


    
    