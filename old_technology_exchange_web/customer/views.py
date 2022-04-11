from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import GetAllCustomerSerializer, CreateCustomerSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class GetAllCustomer(APIView):
    def get(self, request):
        users = User.objects.all()
        json = GetAllCustomerSerializer(users, many=True)
        return Response(data=json.data, status=status.HTTP_200_OK)


class Create(APIView):
    def post(self, request):
        # print(request.data)
        new_data = CreateCustomerSerializer(data=request.data)
        if not new_data.is_valid():
            return Response('Wrong Format', status=status.HTTP_400_BAD_REQUEST)

        new_user = User.objects.create(
            username=new_data.data['username'],
            password=new_data.data['password'],
            gender=new_data.data['gender'],
            phone_number=new_data.data['phone_number'],
            address=new_data.data['address'])
        return Response(data=new_user, status=status.HTTP_201_CREATED)
