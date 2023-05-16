from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

def discover(request):
  context = {
      'parent': 'jobs',
      'segment': 'jobs'
  }
  return render(request, 'pages/pages/jobs/jobs.html', context)


def new_job(request):
  context = {
      'parent': 'jobs',
      'segment': 'new_job'
  }
  return render(request, 'pages/pages/jobs/new-job.html', context)
