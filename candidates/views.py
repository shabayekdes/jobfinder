from django.shortcuts import render


# Create your views here.
def show_profile(request):
    return render(request, 'candidates/show_profile.html', context={})
