# request -> response
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from .graph import *
from .map import *
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import never_cache
from django.http import FileResponse
from django.http import Http404

def index(request):
    return render(request, 'hello.html', { 'name': 'World'})

#The 'X-Frame-Options' header is used to indicate whether or not a browser should be allowed to render a page in an iframe
@never_cache
@xframe_options_exempt 
def graph_view(request):
    locations = cache.get('traceroute_locations')
    print("Graph view called, Locations:", locations)
    # TODO: Remove this hardcoded data
    # locations = [
    # ['12.995479583740234', '79.14990997314453', '182.79.4.225', 'Kātpādi', 'Tamil Nadu', 'India'],
    # ['13.052399635314941', '80.25080108642578', '182.79.14.89', 'Saint Thomas Mount', 'Tamil Nadu', 'India'],
    # ['19.076000213623047', '72.87770080566406', '182.79.134.141', 'Powai', 'Maharashtra', 'India'],
    # ['33.50938034057617', '-112.08255004882812', '62.115.42.118', 'Phoenix', 'Arizona', 'United States'],
    # ['39.043701171875', '-77.47419738769531', '62.115.124.56', 'Ashburn', 'Virginia', 'United States'],
    # ['32.8054313659668', '-96.8142318725586', '80.91.248.157', 'Dallas', 'Texas', 'United States'],
    # ['37.769168853759766', '-122.44249725341797', '192.205.33.25', 'San Francisco', 'California', 'United States'],
    # ['38.906898498535156', '-77.02839660644531', '170.248.56.19', 'Shaw', 'Washington, D.C.', 'United States']
    # ]

    if locations is not None:
        locations.pop(0)
        create_graph(locations, 'mainapp/templates/graph.html')
    try:
        return FileResponse(open('mainapp/templates/graph.html', 'rb'), content_type='text/html')
    except FileNotFoundError:
        raise Http404()

@never_cache
@xframe_options_exempt 
def map_view(request):
    print("Map view called")
    locations = cache.get('traceroute_locations')

    # TODO: Remove this hardcoded data
    # locations = [
    # ['12.995479583740234', '79.14990997314453', '182.79.4.225', 'Kātpādi', 'Tamil Nadu', 'India'],
    # ['13.052399635314941', '80.25080108642578', '182.79.14.89', 'Saint Thomas Mount', 'Tamil Nadu', 'India'],
    # ['19.076000213623047', '72.87770080566406', '182.79.134.141', 'Powai', 'Maharashtra', 'India'],
    # ['33.50938034057617', '-112.08255004882812', '62.115.42.118', 'Phoenix', 'Arizona', 'United States'],
    # ['39.043701171875', '-77.47419738769531', '62.115.124.56', 'Ashburn', 'Virginia', 'United States'],
    # ['32.8054313659668', '-96.8142318725586', '80.91.248.157', 'Dallas', 'Texas', 'United States'],
    # ['37.769168853759766', '-122.44249725341797', '192.205.33.25', 'San Francisco', 'California', 'United States'],
    # ['38.906898498535156', '-77.02839660644531', '170.248.56.19', 'Shaw', 'Washington, D.C.', 'United States']
    # ]

    if locations is not None:
        locations.pop(0)
        plot(locations)
    try:
        return FileResponse(open('mainapp/templates/map.html', 'rb'), content_type='text/html')
    except FileNotFoundError:
        raise Http404()