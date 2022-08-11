import os.path
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, StreamingHttpResponse, HttpResponseRedirect

from .location import find_the_location
from .models import Video, Photo
from .forms import UploadFileForm, CityForm, IPForm
from .recognize import recognize_cat
from .validators import validate_image_form
from .weather import find_the_weather


def base(request):
    context = {
        'title': 'Main page'
    }

    return render(request, 'persik/base.html', context=context)


def play(request):

    return render(request, 'persik/play.html')


def watch(request):
    video_list = Video.objects.all()
    context = {
        'video_list': video_list,
        'title': 'Cat\'s Videos',
    }

    return render(request, 'persik/watch.html', context=context)


def recognize(request):
    error = None
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            photo = Photo()
            photo.file = request.FILES['file']
            if validate_image_form(photo.file):
                photo.save()
            else:
                form = UploadFileForm()
                error = 'The file must be in .jpg, .jpeg, .png and/or less 4mb.'
        else:
            form = UploadFileForm()

    last_photo = Photo.objects.latest('id')

    context = {
        'title': 'Recognize the Cat!',
        'form': form,
        'result': recognize_cat(),
        'photo': last_photo,
        'error': error

    }

    return render(request, 'persik/recognize.html', context=context)


def weather(request):
    result = {}
    error = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            result = find_the_weather(city_name)
            if not result:
                error = 'Such city not found.'
    else:
        form = CityForm()

    context = {
        'title': 'Weather',
        'result': result,
        'form': form,
        'error': error
    }

    return render(request, 'persik/weather.html', context=context)


def location(request):
    error = ''
    if request.method == 'POST':
        form = IPForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip']
            result = find_the_location(ip_address)
            if result:
                return render(request, result)
            else:
                error = 'Incorrect IP address.'

    context = {
        'title': 'LocatioN',
        'error': error
    }

    return render(request, 'persik/location.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>The page not found.</h1>')

# can be added more handlers