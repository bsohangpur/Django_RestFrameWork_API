from django.shortcuts import render
from rest_framework import viewsets, generics
from MainApi.models import Project, Image, Language, Contact, Service, Skill
from MainApi.serializer import ProjectSerializer, ImageSerializer, LanguageSerializer, ContactSerializer
from MainApi.serializer import ServiceSerializer, SkillSerializer

# Create your views here.
# project category view sets...


class LanguageViewSet(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

# project main view sets...


class ProjectViewSet(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# project images view sets...


class ProjectImageViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# contact view sets...


class ContactViewSet(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# service view sets...


class ServiceViewsSet(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# service view sets...


class SkillViewsSet(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
