import requests
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Job, PostJobs

# Get subscription API URL from environment variable or use localhost for development
# For PythonAnywhere: set SUBSCRIPTION_API_URL=https://yourusername.pythonanywhere.com
SUBSCRIPTION_API_URL = os.getenv('SUBSCRIPTION_API_URL', 'https://santhoshrony7.pythonanywhere.com/api/notify')

@receiver(post_save, sender=Job)
def notify_subscribers_on_new_job(sender, instance, created, **kwargs):
    if created:
        # Use job_link if available, else fallback to a default pattern
        job_link = "https://careerly.site"
        try:
            response = requests.post(
                SUBSCRIPTION_API_URL,
                json={"jobLink": job_link},
                timeout=5
            )
            print("Notification sent for Job:", response.status_code, response.text)
        except Exception as e:
            print("Failed to notify subscribers for Job:", e)

@receiver(post_save, sender=PostJobs)
def notify_subscribers_on_new_postjob(sender, instance, created, **kwargs):
    if created:
        job_link = "https://careerly.site"
        try:
            response = requests.post(
                SUBSCRIPTION_API_URL,
                json={"jobLink": job_link},
                timeout=5
            )
            print("Notification sent for PostJobs:", response.status_code, response.text)
        except Exception as e:
            print("Failed to notify subscribers for PostJobs:", e) 