import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constants import Constants

from .models import Blacklist
from .forms import BlacklistForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    blacklists = Blacklist.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(blacklists))

@required_method('GET')
def show(request, blacklist_id) -> JsonResponse:
    blacklist = Blacklist.objects.get(pk=blacklist_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(blacklist))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = BlacklistForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Blacklist successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    blacklist = Blacklist.objects.get(pk=content['id'])
    form = BlacklistForm(instance=blacklist, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Blacklist successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, blacklist_id) -> JsonResponse:
    blacklist = Blacklist.objects.get(pk=blacklist_id)
    blacklist.is_activate = not blacklist.is_activate
    blacklist.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Blacklist successfully activated' if blacklist.is_activate else 'Blacklist successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, blacklist_id) -> JsonResponse:
    blacklist = Blacklist.objects.get(pk=blacklist_id)
    blacklist.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Blacklist successfully deleted.')

