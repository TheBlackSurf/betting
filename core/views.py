from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import *
from .forms import VoteForm
from datetime import datetime

def allvote(request):
    User = get_user_model()
    votes = Vote.objects.all()
    users = User.objects.all()
    context = {
        'users':users,
        'votes':votes,
        'today' : datetime.now(),
    }
    return render(request, 'core/all-vote.html',context)

def alluser(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'core/user/list-user.html',context)

def userdetail(request,pk):
    User = get_user_model()
    votes = Vote.objects.all()
    users = User.objects.get(pk=pk)
    context = {
        'users':users,
        'votes':votes,
    }
    return render(request, 'core/user/user-detail.html',context)


def updatevote(request, pk):
    votes = Vote.objects.get(pk=pk)
    form = VoteForm(instance=votes)
    if request.method == 'POST':
        form = VoteForm(request.POST, instance=votes)
        if form.is_valid():
            form.save()
            return redirect('dash')
    context = {
        'form':form,

    }
    return render(request, 'core/update.html', context)

def vote(request, pk):
    form = VoteForm()
    post = Post.objects.get(pk=pk)
    votes = Vote.objects.all()
    votes.id  = post.id
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect('dash')
    context = {
        'form':form,
        'votes':votes
    }
    return render(request, 'core/edit.html', context)


def postdetail(request):
    post = Post.objects.all()
    context = {
        'post':post,
        'today' : datetime.now(),
    }
    return render(request, 'core/dash.html', context)


