from multiprocessing import context
import pkgutil
from django.shortcuts import redirect, render
from .models import ProfilePoint
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProfilePointForm
# Create your views here.
def viewpoint(request):
    points = ProfilePoint.objects.all()
    
    context = {
        'points':points,
    }
    
    return render(request, 'points/points.html', context)


@staff_member_required(login_url="login")
def addpoints(request):
    form = ProfilePointForm()
    if request.method == "POST":
        form = ProfilePointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewpoint")
    return render(request, "points/add-kolejka.html", {"form": form})

def editpoints(request,pk):
    points = ProfilePoint.objects.get(id=pk)
    form = ProfilePointForm(instance=points)
    if request.method == "POST":
        form = ProfilePointForm(request.POST, instance=points)
        if form.is_valid():
            form.save()
            return redirect("viewpoint")
    return render(request, "points/edit-kolejka.html", {"form": form})