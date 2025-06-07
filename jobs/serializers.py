from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class JobSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'company', 'location', 'job_type', 
                 'salary', 'job_link', 'created_at', 'updated_at', 'creator')
        read_only_fields = ('created_at', 'updated_at') 