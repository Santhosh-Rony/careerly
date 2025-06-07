from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, PostJobsViewSet, admin_dashboard

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'post-jobs', PostJobsViewSet)

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('api/', include(router.urls)),
] 