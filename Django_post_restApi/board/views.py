from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Board
from .serializers import BoardSerializer


def viewjson(request):
    return JsonResponse("Rest API base point...", safe=False)

@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/boardlist/',
        'Detail': '/boardview/<str:pk>/',
        'Create': '/boardinsert/',
        'Update': '/boardupdate/<str:pk>/',
        'Delete': '/boarddelete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def boardList(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)

    return Response(serializer.data)
