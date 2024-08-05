from rest_framework import serializers

from.models import About, Experience, Work, Service, Contact


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'image', 'description']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['image', 'work_place', 'start_finish_year', 'occupation']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['image', 'link', 'price', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['image', 'title', 'description', 'price']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
