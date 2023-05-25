from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rcb(request):
    return HttpResponse ('<h2><marquee>there is a king in this team</marquee></h2>')