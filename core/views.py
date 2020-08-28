from __future__ import unicode_literals
from datetime import datetime
import collections
import csv
import os

# Base Django Imports
from django.shortcuts import render
from django.http.response import JsonResponse

# Rest Framework Imports
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal Imports
from .models import Document
from .serializer import DocumentSerializer
import clickbait_model

# Create your views here.

class DocumentView(APIView):
    def get(self, request, *args, **kargs):
        return Response('lol hi')

    def post(self, request, *args, **kargs):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            title = data['title']
            if data['link']:
                '''
                if link is parsed - scrape the link
                '''
                pass

            return Response(serializer.data)

        return Response(serializer.errors)
        

