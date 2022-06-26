from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField, Textarea
from django.utils import timezone
from datetime import datetime

COLOR = (
    ("Zółty", "Zółty"),
    ("Pomarańczowy", "Pomarańczowy"),
    ("Czerwony", "Czerwony"),
    ("Zielony", "Zielony"),
)

KOLEJKA_CHOICE = (
    ("Kolejka 1", "Kolejka 1"),
    ("Kolejka 2", "Kolejka 2"),
    ("Kolejka 3", "Kolejka 3"),
    ("Kolejka 4", "Kolejka 4"),
    ("Kolejka 5", "Kolejka 5"),
    ("Kolejka 6", "Kolejka 6"),
    ("Kolejka 7", "Kolejka 7"),
    ("Kolejka 8", "Kolejka 8"),
    ("Kolejka 9", "Kolejka 9"),
    ("Kolejka 10", "Kolejka 10"),
    ("Kolejka 11", "Kolejka 11"),
    ("Kolejka 12", "Kolejka 12"),
    ("Kolejka 13", "Kolejka 13"),
    ("Kolejka 14", "Kolejka 14"),
    ("Kolejka 15", "Kolejka 15"),
    ("Kolejka 16", "Kolejka 16"),
    ("Kolejka 17", "Kolejka 17"),
    ("Kolejka 18", "Kolejka 18"),
    ("Kolejka 19", "Kolejka 19"),
    ("Kolejka 20", "Kolejka 20"),
    ("Kolejka 21", "Kolejka 21"),
    ("Kolejka 22", "Kolejka 22"),
    ("Kolejka 23", "Kolejka 23"),
    ("Kolejka 24", "Kolejka 24"),
    ("Kolejka 25", "Kolejka 25"),
    ("Kolejka 26", "Kolejka 26"),
    ("Kolejka 27", "Kolejka 27"),
    ("Kolejka 28", "Kolejka 28"),
    ("Kolejka 29", "Kolejka 29"),
    ("Kolejka 30", "Kolejka 30"),
    ("Kolejka 31", "Kolejka 31"),
    ("Kolejka 32", "Kolejka 32"),
    ("Kolejka 33", "Kolejka 33"),
    ("Kolejka 34", "Kolejka 34"),
)
RESULT = (
    ("za", "za"),
    ("przeciw", 'przeciw'),
)


class Ankieta(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ankieta = models.ForeignKey(Ankieta, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200, choices=RESULT)


class Post(models.Model):
    kolejka = models.CharField(
        max_length=200, choices=KOLEJKA_CHOICE, blank=True, null=True
    )
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ("-created_on",)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.ImageField(
        upload_to="profile-pic",
        null=True,
        blank=True,
        default="profile-pic/profile.png",
    )
    name = models.CharField(max_length=128, null=True, blank=True)
    surnname = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Kolejka(models.Model):
    name = models.CharField(max_length=200, choices=KOLEJKA_CHOICE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f" {self.user.username} zdobył {self.point} punktów  w {self.name}"


class Vote(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    color_vote = models.CharField(
        max_length=200, choices=COLOR, blank=True, null=True)

    
    
    def update(self, *args, **kwargs):
        kwargs.update({"updated": timezone.now})
        super().update(*args, **kwargs)

        return self

    def __str__(self):
        return self.name


class Regulation(models.Model):
    point = models.CharField(max_length=2000)

    def __str__(self):
        return self.point
