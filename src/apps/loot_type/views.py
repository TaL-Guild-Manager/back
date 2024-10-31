import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants
from src.decorators.request_method_validator import required_method

from .models import LootType
from .forms import LootTypeForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    loot_types = LootType.objects.all().values().filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(loot_types))

@required_method('GET')
def show(request, loot_type_id) -> JsonResponse:
    loot_type = LootType.objects.get(pk=loot_type_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(loot_type))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = LootTypeForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'LootType successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    loot_type = LootType.objects.get(pk=content['id'])
    form = LootTypeForm(instance=loot_type, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'LootType successfully updated.')


@required_method('PUT')
@csrf_protect
def activate(request, loot_type_id) -> JsonResponse:
    loot_type = LootType.objects.get(pk=loot_type_id)
    loot_type.is_activate = not loot_type.is_activate
    loot_type.save()

    return api_response(HttpCode.SUCCESS, 'success', 'LootType successfully activated.' if loot_type.is_activate else 'LootType successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, loot_type_id) -> JsonResponse:
    loot_type = LootType.objects.get(pk=loot_type_id)
    loot_type.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'LootType successfully deleted.')