from django.urls import path
from yogi.views import *
urlpatterns = [
    path('',my_view, name='my_view'),
    path('contact/',contact_i, name='contact'),
    path('about/',abou_t,name='about')
]