from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all().prefetch_related("images")
  
    return render(request, "index.html", {'projects':projects})

def project_details(request, pk):

    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, "project.html", context)