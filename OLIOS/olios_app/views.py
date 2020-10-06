from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import SpaceObject

def index(request):
    space_object_list = SpaceObject.objects.order_by('launch_date')[:5]
    context = {
        'space_object_list' : space_object_list,
    }
    return render(request, 'index.html', context)

def post(request, post_id):
    return HttpResponse("You're looking at post %s." % question_id)

