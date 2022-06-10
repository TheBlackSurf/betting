from datetime import datetime

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewUserForm, PostForm, RFPAuthForm, VoteForm
from .models import *


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


def login_request(request):
    if request.method == "POST":
        form = RFPAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dash")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = RFPAuthForm()
    return render(
        request=request, template_name="core/login.html", context={"login_form": form}
    )


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="core/register.html",
        context={"register_form": form},
    )


@login_required(login_url="login")
def allvote(request):
    User = get_user_model()
    votes = Vote.objects.all()
    users = User.objects.all()
    context = {
        "users": users,
        "votes": votes,
        "today": datetime.now(),
    }
    return render(request, "core/all-vote.html", context)


@staff_member_required(login_url="login")
def alluser(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "core/user/list-user.html", context)


@staff_member_required(login_url="login")
def userdetail(request, pk):
    User = get_user_model()
    votes = Vote.objects.all()
    users = User.objects.get(id=pk)
    context = {
        "users": users,
        "votes": votes,
    }
    return render(request, "core/user/user-detail.html", context)


@login_required(login_url="login")
def updatevote(request, pk):
    votes = Vote.objects.get(pk=pk)
    form = VoteForm(instance=votes)
    if request.method == "POST":
        form = VoteForm(request.POST, instance=votes)
        if form.is_valid():
            form.save()
            return redirect("dash")
    context = {
        "form": form,
    }
    return render(request, "core/update.html", context)


@login_required(login_url="login")
def vote(request, pk):
    form = VoteForm()
    post = Post.objects.get(pk=pk)
    votes = Vote.objects.all()
    votes.id = post.id
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post = post
            form.save()
            return redirect("dash")
    context = {
        "form": form,
        "votes": votes,
        "post": post,
    }
    return render(request, "core/edit.html", context)


@login_required(login_url="login")
def postdetail(request):
    post = Post.objects.all()
    User = get_user_model()
    users = User.objects.all()

    context = {
        "post": post,
        "today": datetime.now(),
        "users": users,
        "count": Post.objects.count(),
    }
    return render(request, "core/dash.html", context)


@staff_member_required(login_url="login")
def addpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("dash")
    return render(request, "core/add-post.html", {"form": form})


@staff_member_required(login_url="login")
def deletepost(request, *args, **kwargs):
    pk = kwargs.get("pk")
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("/")

    return render(request, "core/deletepost.html")


@login_required(login_url="login")
def deletevote(request, *args, **kwargs):
    pk = kwargs.get("pk")
    vote = get_object_or_404(Vote, id=pk)

    if request.method == "POST":
        vote.delete()
        return redirect("/")

    return render(request, "core/deletevote.html")
