from datetime import datetime
from multiprocessing import context

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .filters import PostFilter
from .forms import (
    KolejkaForm,
    NewUserForm,
    PostForm,
    ProfileForm,
    RegulationForm,
    RFPAuthForm,
    VoteColorForm,
    VoteForm,
    ResultForm,
    AnkietaForm,
)
from .models import Kolejka, Post, Profile, Regulation, Vote, Ankieta, Result



def deleteResult(request, pk):
    result = Result.objects.get(id=pk)
    if request.method == "POST":
        if result.user == request.user:
            print(result.ankieta.title)
            result.delete()
            return redirect("ankieta")
        else:
            return redirect("ankieta")

    return render(
        request,
        "core/delete-result.html",
        {
            "result": result,
        },
    )


def editAnkieta(request, pk):
    form = ResultForm()
    ankieta = Ankieta.objects.get(id=pk)
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.ankieta = ankieta
            form.save()
            return redirect("ankieta")
    return render(
        request,
        "core/edit-ankieta.html",
        {
            "ankieta": ankieta,
            "form": form,
        },
    )


def showAnkieta(request):
    ankiety = Ankieta.objects.all()
    results = Result.objects.all()
    form = AnkietaForm()
    if request.method == "POST":
        form = AnkietaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ankieta")
    return render(
        request,
        "core/ankieta.html",
        {
            "ankiety": ankiety,
            "results": results,
            "form": form,
        },
    )


@staff_member_required(login_url="login")
def editregulation(request, pk):
    regulations = Regulation.objects.get(id=pk)
    form = RegulationForm(instance=regulations)
    if request.method == "POST":
        form = RegulationForm(request.POST, instance=regulations)
        if form.is_valid():
            form.save()
            return redirect("regulation")
    context = {"regulations": regulations, "form": form}
    return render(request, "core/edit-regulamin.html", context)


@login_required(login_url="login")
def setting_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dash")
    return render(
        request,
        "core/edit-profile.html",
        {
            "profile": profile,
            "form": form,
        },
    )


def profile_settings(request):
    return {
        # 'profile_user': Profile.objects.filter(user=request.user)
        "profile_user": Profile.objects.all()
    }


@login_required(login_url="login")
def regulation(request):
    regulations = Regulation.objects.all()
    form = RegulationForm()
    if request.method == "POST":
        form = RegulationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("regulation")
    context = {"regulations": regulations, "form": form}
    return render(request, "core/regulamin.html", context)


@staff_member_required(login_url="login")
def deleteregulation(request, pk):
    regulations = Regulation.objects.get(id=pk)
    if request.method == "POST":
        regulations.delete()
        return redirect("regulation")
    context = {
        "regulations": regulations,
    }
    return render(request, "core/delete-regulamin.html", context)


@staff_member_required(login_url="login")
def addkolejka(request):
    form = KolejkaForm()
    if request.method == "POST":
        form = KolejkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kolejka")
    return render(request, "core/add-kolejka.html", {"form": form})


@login_required(login_url="login")
def kolejka(request):
    User = get_user_model()
    users = User.objects.all()
    kolejki = Kolejka.objects.all()

    context = {
        "kolejki": kolejki,
        "users": users,
    }
    return render(request, "core/kolejka.html", context)


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
            messages.success(request, "Pomyślnie")
            Profile.objects.create(user=user)
            if not user:
                raise form.ValidationError("User does not exist.")
            if not user.is_active:
                raise form.ValidationError("User is no longer active.")
            return redirect("login")
        messages.error(
            request,
            """
            Błędy w Formularzu!
            """,
        )
    form = NewUserForm()
    return render(
        request=request,
        template_name="core/register.html",
        context={"register_form": form},
    )


@login_required(login_url="login")
def allvote(request):
    User = get_user_model()
    votes = Vote.objects.order_by("author")
    posts = Post.objects.all()
    users = User.objects.all()

    if request.method == "POST":
        kolejka = request.POST.get("kolejka")
        kolor = request.POST.get("kolor")
        wynik = request.POST.get("wynik")

        votes = Vote.objects.order_by("author")
        votes_filter = votes.filter(post__body=kolejka)
        votes_filter.filter(name=wynik).update(color_vote=kolor)
        print(votes_filter)
        return redirect("allvote")

    context = {
        "users": users,
        "votes": votes,
        "posts": posts,
        "today": datetime.now(),
    }
    return render(request, "core/all-vote.html", context)


@staff_member_required(login_url="login")
def editVote(request, pk):
    votes = Vote.objects.get(id=pk)
    form = VoteColorForm(instance=votes)
    if request.method == "POST":
        form = VoteColorForm(request.POST, instance=votes)
        if form.is_valid():
            form.save()
            return redirect("allvote")
    return render(
        request,
        "core/edit-vote.html",
        {
            "votes": votes,
            "form": form,
        },
    )


@staff_member_required(login_url="login")
def alluser(request):
    User = get_user_model()
    users = User.objects.order_by("username").exclude(username='admin')
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
    votes = Vote.objects.get(id=pk)
    form = VoteForm(instance=votes)
    if request.method == "POST":
        form = VoteForm(request.POST, instance=votes)
        if form.is_valid():
            form.save()
            return redirect("dash")
    context = {
        "form": form,
        "votes": votes,
    }
    return render(request, "core/update.html", context)


@login_required(login_url="login")
def addvote(request, pk):
    form = VoteForm()
    datetimes = datetime.now().strftime("Y-m-d H:i:s")
    post = Post.objects.get(pk=pk)
    posttimes = post.created_on.strftime("Y-m-d H:i:s")
    votes = Vote.objects.all()
    votes.id = post.id

    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post = post
            if form.instance.post.created_on.strftime(
                "Y-m-d H:i:s"
            ) >= timezone.now().strftime("Y-m-d H:i:s"):
                form.save()
            else:
                redirect("dash")
            return redirect("dash")
    context = {
        "form": form,
        "votes": votes,
        "post": post,
        "datetimes": datetimes,
        "posttimes": posttimes,
        "today": datetime.now(),
    }
    return render(request, "core/edit.html", context)


@login_required(login_url="login")
def postdetail(request):
    post = Post.objects.order_by("-created_on")
    User = get_user_model()
    users = User.objects.all()
    myFilter = PostFilter(request.GET, queryset=post)
    post = myFilter.qs
    context = {
        "post": post,
        "today": datetime.now(),
        "users": users,
        "count": Post.objects.count(),
        "myFilter": myFilter,
    }
    return render(request, "core/dash.html", context)


@staff_member_required(login_url="login")
def addpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, initial={"kolejka": "kolejka"})
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

    return render(
        request,
        "core/deletevote.html",
        {
            "vote": vote,
        },
    )
