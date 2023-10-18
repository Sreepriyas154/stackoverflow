from rest_framework import serializers
from django.contrib.auth.models import User




class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fileds=["first_name","last_name","email","password"]

        def create(self,validates_data):
            return User.objects.create_user(User,**validates_data)