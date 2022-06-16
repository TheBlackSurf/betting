from django.shortcuts import redirect, render
from .models import Info
# Create your views here.
from .forms import InfoForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def info(request):
    infos = Info.objects.all()
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    context = {
        'infos': infos,
        'form': form
    }
    return render(request, 'info/info.html', context)


@staff_member_required(login_url="login")
def editInfo(request, pk):
    infos = Info.objects.get(id=pk)
    form = InfoForm(instance=infos)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=infos)
        if form.is_valid():
            form.save()
            return redirect('info')
    context = {
        'infos': infos,
        'form': form
    }
    return render(request, 'info/edit-info.html', context)


@staff_member_required(login_url="login")
def deleteInfo(request, pk):
    infos = Info.objects.get(id=pk)
    if request.method == 'POST':
        infos.delete()
        return redirect('info')
    context = {
        'infos': infos,

    }
    return render(request, 'info/delete-info.html', context)
