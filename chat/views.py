from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Message
from .serializers import MessageSerializer

# Create your views here.

def room(request, room_name):
    return render(request, 'chat/index.html', {
        'room_name': room_name
    })

@csrf_exempt
@api_view(['GET'])
def chatGet(request, room):
    chat_obj = Message.objects.filter(thread=room)
    print(chat_obj)
    response = {}
    response_array = []

    for k in chat_obj:
        response_array.append( {"msg": k.text, "id": k.sender})
          
    print(response_array)
    return  Response(response_array)
    
    # chat_obj = Message.objects.filter(thread=room)
   

