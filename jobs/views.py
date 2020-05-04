from django.shortcuts import render
from .models import Job
# Create your views here.
def profile(request):
    jobs = Job.objects
    return render(request,'jobs/profile.html', {'jobs': jobs})