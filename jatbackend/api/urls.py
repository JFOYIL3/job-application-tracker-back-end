from django.urls import path
from .views import job_application_view


urlpatterns = [
    # JOB APPLICATIONS
    path('job-applications', job_application_view.JobApplicationListView.as_view(),
         name='job-applications'),
    path('job-applications/<str:id>', job_application_view.JobApplicationDetailView.as_view(),
         name='job-application-detail'),
    path('job-applications', job_application_view.JobApplicationCreateView.as_view(),
         name='job-application-create'),
    path('job-applications/<str:id>', job_application_view.JobApplicationUpdateView.as_view(),
         name='job-application-update'),
    path('job-applications/<str:id>', job_application_view.JobApplicationDeleteView.as_view(),
         name='job-application-delete'),
]
