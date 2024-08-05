from rest_framework import generics, permissions
from .models import About, Experience, Work, Service, Contact
from .serializers import AboutSerializer, ExperienceSerializer, WorkSerializer, ServiceSerializer, ContactSerializer


class AboutListCreateView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
