import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants
from src.decorators.request_method_validator import required_method

from .models import CombatType
from .forms import CombatTypeForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    combat_types = CombatType.objects.all().values().filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(combat_types))

@required_method('GET')
def show(request, combat_type_id) -> JsonResponse:
    combat_type = CombatType.objects.get(pk=combat_type_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(combat_type))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = CombatTypeForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'CombatType successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    combat_type = CombatType.objects.get(pk=content['id'])
    form = CombatTypeForm(instance=combat_type, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'CombatType successfully updated.')


@required_method('PUT')
@csrf_protect
def activate(request, combat_type_id) -> JsonResponse:
    combat_type = CombatType.objects.get(pk=combat_type_id)
    combat_type.is_activate = not combat_type.is_activate
    combat_type.save()

    return api_response(HttpCode.SUCCESS, 'success', 'CombatType successfully activated.' if combat_type.is_activate else 'CombatType successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, combat_type_id) -> JsonResponse:
    combat_type = CombatType.objects.get(pk=combat_type_id)
    combat_type.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'CombatType successfully deleted.')