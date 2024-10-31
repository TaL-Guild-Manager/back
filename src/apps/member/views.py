import json

from datetime import datetime
from zoneinfo import ZoneInfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constant import Constants

from .models import Member
from .forms import MemberForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    members = Member.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(members))

@required_method('GET')
def show(request, member_id) -> JsonResponse:
    member = Member.objects.get(pk=member_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(member))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = MemberForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Member successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    member = Member.objects.get(pk=content['id'])
    form = MemberForm(instance=member, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Member successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, member_id) -> JsonResponse:
    member = Member.objects.get(pk=member_id)
    member.is_activate = not member.is_activate
    member.removed_at = None if member.removed_at else datetime.now(ZoneInfo("Europe/Paris"))
    member.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Member successfully activated' if member.is_activate else 'Member successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, member_id) -> JsonResponse:
    member = Member.objects.get(pk=member_id)
    member.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Member successfully deleted.')
