from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=200)
    company_logo = models.URLField(blank=True, null=True)
    job_link = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)  # e.g., Onsite, Remote
    salary = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    posted_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    company_backed_by = models.CharField(max_length=200, blank=True, null=True)  # e.g., "Y COMBINATOR"
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs', null=True)

    class Meta:
        ordering = ['-is_featured', '-posted_date', '-created_at']

    def __str__(self):
        return f"{self.title} at {self.company}"


class PostJobs(models.Model):
    """
    New model for post-jobs with the specified fields
    """
    title = models.CharField(max_length=200, help_text="Job title")
    company = models.CharField(max_length=200, help_text="Company name")
    job_link = models.URLField(help_text="Application link")
    location = models.CharField(max_length=200, help_text="Job location", blank=True, null=True)
    experience = models.CharField(max_length=100, help_text="Required experience level", blank=True, null=True)
    job_type = models.CharField(
        max_length=100, 
        choices=[
            ('full-time', 'Full Time'),
            ('part-time', 'Part Time'),
            ('contract', 'Contract'),
            ('remote', 'Remote'),
            ('hybrid', 'Hybrid'),
            ('onsite', 'Onsite'),
        ],
        help_text="Type of job",
        blank=True,
        null=True
    )
    salary = models.CharField(max_length=100, help_text="Salary range", blank=True, null=True)
    posted_date = models.DateField(default=timezone.now, help_text="Date when job was posted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='post_jobs',
        help_text="User who created this job post"
    )

    class Meta:
        ordering = ['-posted_date', '-created_at']
        verbose_name = "Post Job"
        verbose_name_plural = "Post Jobs"

    def __str__(self):
        return f"{self.title} at {self.company}"
