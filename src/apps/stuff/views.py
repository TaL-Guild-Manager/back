import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constants import Constants

from .models import Stuff
from .forms import StuffForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    stuffs = Stuff.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(stuffs))

@required_method('GET')
def show(request, stuff_id) -> JsonResponse:
    stuff = Stuff.objects.get(pk=stuff_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(stuff))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = StuffForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Stuff successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    stuff = Stuff.objects.get(pk=content['id'])
    form = StuffForm(instance=stuff, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Stuff successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, stuff_id) -> JsonResponse:
    stuff = Stuff.objects.get(pk=stuff_id)
    stuff.is_activate = not stuff.is_activate
    stuff.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Stuff successfully activated' if stuff.is_activate else 'Stuff successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, stuff_id) -> JsonResponse:
    stuff = Stuff.objects.get(pk=stuff_id)
    stuff.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Stuff successfully deleted.')

