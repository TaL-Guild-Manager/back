import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants
from src.decorators.request_method_validator import required_method

from .models import Boss
from .forms import BossForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    bosses = Boss.objects.all().values().filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(bosses))

@required_method('GET')
def show(request, boss_id) -> JsonResponse:
    boss = Boss.objects.get(pk=boss_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(boss))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = BossForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Boss successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    boss = Boss.objects.get(pk=content['id'])
    form = BossForm(instance=boss, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Boss successfully updated.')


@required_method('PUT')
@csrf_protect
def activate(request, boss_id) -> JsonResponse:
    boss = Boss.objects.get(pk=boss_id)
    boss.is_activate = not boss.is_activate
    boss.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Boss successfully activated.' if boss.is_activate else 'Boss successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, boss_id) -> JsonResponse:
    boss = Boss.objects.get(pk=boss_id)
    boss.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Boss successfully deleted.')