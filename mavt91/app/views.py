from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import re
from django.contrib.gis.geos import Point


from .models import Coordinates


def base(request):
    template = 'mapping/base.html'
    context = {
    }
    return render(request, template, context)


def mapping(request):
    template = 'mapping/mapping.html'
    token = request.COOKIES.get('csrftoken')
    context = {
        'csrf_token': token,
    }
    return render(request, template, context)


def input_coordinate_db(request):
    if request.is_ajax():
        str = request.body.decode('utf-8')
        pattern = '(\d{2}.\d*)'
        coor1, coor2 = re.findall(pattern, str)
        coor1, coor2 = float(coor1), float(coor2)
        Coordinates.objects.create(coordinates=Point((coor1, coor2)))
    return HttpResponse(request)


def show_coordinates(request):
    template = 'mapping/show_coordinates.html'
    data = list(Coordinates.objects.all())
    paginator = Paginator(data, 100)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'data': contacts,
    }
    return render(request, template, context)
