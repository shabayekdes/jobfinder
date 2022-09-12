from django.shortcuts import render

from jobs.models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all()

    context = {
        'jobs': jobs
    }
    return render(request, 'home.html', context)
