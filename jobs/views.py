from django.shortcuts import render, get_object_or_404

from jobs.models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'home.html', context)


def list_job(request):
    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/list.html', context)


def show_job(request, id=id):
    job = get_object_or_404(Job, id=id)

    context = {
        'job': job
    }
    return render(request, 'jobs/show.html', context)
