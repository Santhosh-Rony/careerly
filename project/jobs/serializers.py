from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job, PostJobs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class JobSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'company', 'job_link', 
            'location', 'experience', 'job_type', 'salary', 
            'posted_date', 'created_at', 'updated_at', 'creator'
        ]
        read_only_fields = ['created_at', 'updated_at']

class PostJobsSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = PostJobs
        fields = [
            'id', 'title', 'company', 'job_link', 'location', 
            'experience', 'job_type', 'salary', 'posted_date', 
            'created_at', 'updated_at', 'creator'
        ]
        read_only_fields = ['created_at', 'updated_at'] 
