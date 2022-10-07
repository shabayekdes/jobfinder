from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from candidates.forms import CandidateForm
from jobs.models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all()[:5]
    register_form = CandidateForm(request.POST or None)
    if register_form.is_valid():
        user = register_form.save()
        login(request, user)
        return redirect("candidates:show_profile")

    context = {
        'jobs': jobs,
        'register_form': register_form
    }
    return render(request, 'home.html', context)


class JobListView(ListView):
    model = Job
    template_name = 'jobs/list.html'
    paginate_by = 15


def show_job(request, id=id):
    job = get_object_or_404(Job, id=id)
    list_jobs = Job.objects.order_by('?').exclude(id=id)[:5]

    context = {
        'job': job,
        'list_jobs': list_jobs
    }
    return render(request, 'jobs/show.html', context)
