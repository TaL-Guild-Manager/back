import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constant import Constants

from .models import Loot
from .forms import LootForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    loots = Loot.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(loots))

@required_method('GET')
def show(request, loot_id) -> JsonResponse:
    loot = Loot.objects.get(pk=loot_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(loot))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = LootForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Loot successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    loot = Loot.objects.get(pk=content['id'])
    form = LootForm(instance=loot, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Loot successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, loot_id) -> JsonResponse:
    loot = Loot.objects.get(pk=loot_id)
    loot.is_activate = not loot.is_activate
    loot.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Loot successfully activated' if loot.is_activate else 'Loot successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, loot_id) -> JsonResponse:
    loot = Loot.objects.get(pk=loot_id)
    loot.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Loot successfully deleted.')

