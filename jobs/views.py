from django.core.paginator import Paginator
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
    query = request.GET.get('q')
    if query is None:
        jobs = Job.objects.all()
    else:
        jobs = Job.objects.search(query)

    paginator = Paginator(jobs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {
        'jobs': page_obj
    }
    return render(request, 'jobs/list.html', context)


def show_job(request, id=id):
    job = get_object_or_404(Job, id=id)

    context = {
        'job': job
    }
    return render(request, 'jobs/show.html', context)
