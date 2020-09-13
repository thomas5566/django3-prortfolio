from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def home(request):
    # grabs everython from DB
    projects = Project.objects.all()
    return render(request, "porfolio/home.html", {"projects": projects})
