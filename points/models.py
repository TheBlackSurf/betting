from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.db import models


class AnnotationManager(models.Manager):

    def __init__(self, **kwargs):
        super().__init__()
        self.annotations = kwargs

    def get_queryset(self):
        return super().get_queryset().annotate(**self.annotations)


class ProfilePoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kolejka1 = models.IntegerField(null=True, blank=True, default=0)
    kolejka2 = models.IntegerField(null=True, blank=True, default=0)
    kolejka3 = models.IntegerField(null=True, blank=True, default=0)
    kolejka4 = models.IntegerField(null=True, blank=True, default=0)
    kolejka5 = models.IntegerField(null=True, blank=True, default=0)
    kolejka6 = models.IntegerField(null=True, blank=True, default=0)
    kolejka7 = models.IntegerField(null=True, blank=True, default=0)
    kolejka8 = models.IntegerField(null=True, blank=True, default=0)
    kolejka9 = models.IntegerField(null=True, blank=True, default=0)
    kolejka10 = models.IntegerField(null=True, blank=True, default=0)
    kolejka11 = models.IntegerField(null=True, blank=True, default=0)
    kolejka12 = models.IntegerField(null=True, blank=True, default=0)
    kolejka13 = models.IntegerField(null=True, blank=True, default=0)
    kolejka14 = models.IntegerField(null=True, blank=True, default=0)
    kolejka15 = models.IntegerField(null=True, blank=True, default=0)
    kolejka16 = models.IntegerField(null=True, blank=True, default=0)
    kolejka17 = models.IntegerField(null=True, blank=True, default=0)
    kolejka18 = models.IntegerField(null=True, blank=True, default=0)
    kolejka19 = models.IntegerField(null=True, blank=True, default=0)
    kolejka20 = models.IntegerField(null=True, blank=True, default=0)
    kolejka21 = models.IntegerField(null=True, blank=True, default=0)
    kolejka22 = models.IntegerField(null=True, blank=True, default=0)
    kolejka23 = models.IntegerField(null=True, blank=True, default=0)
    kolejka24 = models.IntegerField(null=True, blank=True, default=0)
    kolejka25 = models.IntegerField(null=True, blank=True, default=0)
    kolejka26 = models.IntegerField(null=True, blank=True, default=0)
    kolejka27 = models.IntegerField(null=True, blank=True, default=0)
    kolejka28 = models.IntegerField(null=True, blank=True, default=0)
    kolejka29 = models.IntegerField(null=True, blank=True, default=0)
    kolejka30 = models.IntegerField(null=True, blank=True, default=0)
    kolejka31 = models.IntegerField(null=True, blank=True, default=0)
    kolejka32 = models.IntegerField(null=True, blank=True, default=0)
    kolejka33 = models.IntegerField(null=True, blank=True, default=0)
    kolejka34 = models.IntegerField(null=True, blank=True, default=0)
    dodatkowepunkty = models.IntegerField(null=True, blank=True, default=0)

    objects = AnnotationManager(
        gross=F('kolejka1')+F('kolejka2')+F('kolejka3')+F('kolejka4')+F('kolejka5')+F('kolejka6')+F('kolejka7')+F('kolejka8')+F('kolejka9')+F('kolejka10')+F('kolejka11')+F('kolejka12')+F('kolejka13')+F('kolejka14')+F('kolejka15')+F('kolejka16')+F('kolejka17') +
        F('kolejka18')+F('kolejka19')+F('kolejka20')+F('kolejka21')+F('kolejka22')+F('kolejka23')+F('kolejka24')+F('kolejka25') +
        F('kolejka26')+F('kolejka27')+F('kolejka28')+F('kolejka29') +
        F('kolejka30')+F('kolejka31') +
        F('kolejka32')+F('kolejka33')+F('kolejka34')+F('dodatkowepunkty'),
    )
