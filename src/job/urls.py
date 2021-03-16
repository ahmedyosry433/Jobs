from django.urls import include, path
from . import views
app_name = 'job'

urlpatterns = [
    path('', views.index, name='index'),
    path('joblist/', views.job_list, name='job_list'),
    path('addjob/', views.add_job, name='add_job'),
    path('<str:slug>', views.job_details, name='job_details'),

]
