from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import Job, PostJobs
from .serializers import JobSerializer, PostJobsSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

@staff_member_required
def admin_dashboard(request):
    """Admin welcome landing page with dashboard overview"""
    today = timezone.now().date()
    
    # Get job statistics
    total_jobs = Job.objects.count()
    recent_jobs = Job.objects.filter(created_at__date=today).count()
    active_jobs = Job.objects.filter(is_active=True).count() if hasattr(Job, 'is_active') else total_jobs
    
    # Get PostJobs statistics
    total_post_jobs = PostJobs.objects.count()
    recent_post_jobs = PostJobs.objects.filter(created_at__date=today).count()
    
    # Get recent jobs for display
    latest_jobs = Job.objects.all().order_by('-created_at')[:5]
    latest_post_jobs = PostJobs.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_jobs': total_jobs,
        'recent_jobs': recent_jobs,
        'active_jobs': active_jobs,
        'total_post_jobs': total_post_jobs,
        'recent_post_jobs': recent_post_jobs,
        'latest_jobs': latest_jobs,
        'latest_post_jobs': latest_post_jobs,
        'today': today,
    }
    
    return render(request, 'admin/admin_dashboard.html', context)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=False, methods=['get'])
    def my_jobs(self, request):
        jobs = Job.objects.filter(creator=request.user).order_by('-created_at')
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        jobs = Job.objects.filter(title__icontains=query) | \
               Job.objects.filter(description__icontains=query) | \
               Job.objects.filter(company__icontains=query) | \
               Job.objects.filter(location__icontains=query)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)

class PostJobsViewSet(viewsets.ModelViewSet):
    queryset = PostJobs.objects.all().order_by('-created_at')
    serializer_class = PostJobsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=False, methods=['get'])
    def my_post_jobs(self, request):
        post_jobs = PostJobs.objects.filter(creator=request.user).order_by('-created_at')
        serializer = self.get_serializer(post_jobs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        post_jobs = PostJobs.objects.filter(
            Q(title__icontains=query) | 
            Q(company__icontains=query) | 
            Q(location__icontains=query) |
            Q(experience__icontains=query) |
            Q(job_type__icontains=query)
        ).order_by('-created_at')
        serializer = self.get_serializer(post_jobs, many=True)
        return Response(serializer.data)
