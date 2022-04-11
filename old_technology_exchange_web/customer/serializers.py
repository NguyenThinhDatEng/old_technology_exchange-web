from rest_framework import serializers
from .models import User
# convert data of model to json


class GetAllCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'gender', 'phone_number', 'address')


class CreateCustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",

        error_messages={
            "unique": "A user with that username already exists.",
        },)
    password = serializers.CharField(max_length=20)
    sex_choices = ((0, 'Male'), (1, 'Female'), (2, 'Unknown'))
    gender = serializers.ChoiceField(sex_choices)
    phone_number = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'password', 'gender', 'phone_number', 'address')
