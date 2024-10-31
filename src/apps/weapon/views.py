import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants
from src.decorators.request_method_validator import required_method

from .models import Weapon
from .forms import WeaponForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    weapons = Weapon.objects.all().values().filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(weapons))

@required_method('GET')
def show(request, weapon_id) -> JsonResponse:
    weapon = Weapon.objects.get(pk=weapon_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(weapon))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = WeaponForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Weapon successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    weapon = Weapon.objects.get(pk=content['id'])
    form = WeaponForm(instance=weapon, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Weapon successfully updated.')


@required_method('PUT')
@csrf_protect
def activate(request, weapon_id) -> JsonResponse:
    weapon = Weapon.objects.get(pk=weapon_id)
    weapon.is_activate = not weapon.is_activate
    weapon.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Weapon successfully activated' if weapon.is_activate else 'Weapon successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, weapon_id) -> JsonResponse:
    weapon = Weapon.objects.get(pk=weapon_id)
    weapon.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Weapon successfully deleted.')