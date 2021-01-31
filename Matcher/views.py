from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from . import serializers, models
from rest_framework.response import Response
from rest_framework import status
from fp import *
import cv2
from foldercopy import *
from django.core.files.storage import default_storage
# Create your views here.

class ProfileViews(APIView):
    serializer_class = serializers.ProfileSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request, format=None):
        queryset = models.Profile.objects.all()
        serializer = serializers.ProfileSerializer(queryset, many=True)
        # data = serializer.data
        # print(data[0].get('name'))
        return Response(serializer.data)

    #To input pharamacy details of particular user
    def post(self, request, format=None):
        serializer = serializers.ProfileSerializer(data = request.data)         
        
        if serializer.is_valid():
            # print('\n',serializer.validated_data['name'])
            # print('\n',serializer.validated_data['fingerprint'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchView(APIView):
    serializer_class = serializers.MatchSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request, format=None):
        queryset = models.Profile.objects.all()
        serializer = serializers.MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = serializers.MatchSerializer(data = request.data)

        if serializer.is_valid():
            # print('\n',type(str(serializer.validated_data['fingerprint'])))
            queryset = models.Profile.objects.all()
            serializer2 = serializers.ProfileSerializer(queryset, many=True)
            data = serializer2.data
            result = 'null'

            if(os.path.exists('FingerImage.bmp')):
                # os.remove('C:/Users/Sourabh/Fingerprints/FingerImage.bmp')
                home = os.path.expanduser('~')
                os.remove(os.path.join(home, 'Fingerprints/FingerImage.bmp'))
           
            file = request.FILES['fingerprint']
            file_name = default_storage.save(file.name, file)

            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)


            fImage = cv2.imread(str(file))

            # print(str(serializer.validated_data['fingerprint']))
            # print('\n', type(request.FILES['fingerprint']))
            # print('\n', file, file_url)

            for i in range(len(data)):
                print(data[i].get('fingerprint'))
                DbImage = cv2.imread('C:/Users/Sourabh/Fingerprints' + data[i].get('fingerprint'))

                if(isMatch(fImage, DbImage)):
                    result = data[i].get('name')
                    break
            # os.remove(str(file))
            return Response(result)