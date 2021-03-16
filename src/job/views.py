from django.shortcuts import redirect, render
from .models import job
from django.core.paginator import Paginator
from .form import ApplyForm, AddForm
from django.urls import reverse


# Create your views here.


def index(request):

    return render(request, 'job/index.html')

########################################################################################
# Page Job-List


def job_list(request):
    job_list = job.objects.all()  # Query

    paginator = Paginator(job_list, 3)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}  # Templates اللي رايح لل

    return render(request, 'job/job_list.html', context)

########################################################################################
# Page Job-Detials


def job_details(request, slug):

    job_details = job.objects.get(slug=slug)

    # form

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.Job = job_details  # Job foreignkey not class name
            myform.save()

    else:
        form = ApplyForm()

    context = {'job': job_details, 'form1': form}  # Templates اللي رايح لل
    return render(request, 'job/job_details.html', context)

########################################################################################
# Add_Job


def add_job(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = AddForm()

    return render(request, 'job/add_job.html', {'form': form})
