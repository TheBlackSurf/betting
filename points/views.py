from django.shortcuts import redirect, render
from .models import ProfilePoint
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProfilePointForm
from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def viewpoint(request):
    points = ProfilePoint.objects.all()
    labels = []
    data = []
    for p in points:
        labels.append(p.user.username)
        data.append(p.gross)
    context = {
        'points': points,
        'labels': labels,
        'data': data,
        
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


@staff_member_required(login_url="login")
def editpoints(request, pk):
    points = ProfilePoint.objects.get(id=pk)
    form = ProfilePointForm(instance=points)
    if request.method == "POST":
        form = ProfilePointForm(request.POST, instance=points)
        if form.is_valid():
            form.save()
            return redirect("viewpoint")
    return render(request, "points/edit-kolejka.html", {"form": form})
