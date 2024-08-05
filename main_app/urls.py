from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutListCreateView.as_view(), name='about-list-create'),
    path('experience/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('work/', WorkListCreateView.as_view(), name='work-list-create'),
    path('service/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('contact/', ContactListCreateView.as_view(), name='contact-list-create'),
]
