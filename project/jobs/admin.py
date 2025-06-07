from django.contrib import admin
from .models import Job, PostJobs

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date', 'created_at')
    list_filter = ('posted_date', 'location')
    search_fields = ('title', 'company', 'location', 'tags')
    date_hierarchy = 'posted_date'
    ordering = ('-posted_date', '-created_at')


@admin.register(PostJobs)
class PostJobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'salary', 'posted_date', 'creator')
    list_filter = ('job_type', 'posted_date', 'location', 'creator')
    search_fields = ('title', 'company', 'location', 'experience')
    date_hierarchy = 'posted_date'
    ordering = ('-posted_date', '-created_at')
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company', 'job_link', 'location')
        }),
        ('Job Details', {
            'fields': ('experience', 'job_type', 'salary')
        }),
        ('Dates', {
            'fields': ('posted_date',),
            'classes': ('collapse',)
        }),
        ('System Info', {
            'fields': ('creator',),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.creator:
            obj.creator = request.user
        super().save_model(request, obj, form, change)
