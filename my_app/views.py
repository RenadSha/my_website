from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all().prefetch_related("images")
    project = Project.objects.first()
    return render(request, "index.html", {'projects':projects, 'project':project})