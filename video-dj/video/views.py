from django.shortcuts import render

# Create your views here.
from .models import Video


def index(request):
    video = Video.objects.all()
    return render(request , 'index.html', {
        'video': video
    })