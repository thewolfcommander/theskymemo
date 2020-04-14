from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about-me/', about, name='about'),
    path('contact-me/', contact, name='contact'),
    path('typography/', typography, name='typography'),
    path('blog/home/', blog, name='blog'),
    path('blog/single/', single, name='single'),
]