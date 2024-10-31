import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constant import Constants

from .models import Roadster
from .forms import RoadsterForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    roadsters = Roadster.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(roadsters))

@required_method('GET')
def show(request, roadster_id) -> JsonResponse:
    roadster = Roadster.objects.get(pk=roadster_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(roadster))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = RoadsterForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Roadster successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    roadster = Roadster.objects.get(pk=content['id'])
    form = RoadsterForm(instance=roadster, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Roadster successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, roadster_id) -> JsonResponse:
    roadster = Roadster.objects.get(pk=roadster_id)
    roadster.is_activate = not roadster.is_activate
    roadster.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Roadster successfully activated' if roadster.is_activate else 'Roadster successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, roadster_id) -> JsonResponse:
    member = Roadster.objects.get(pk=roadster_id)
    member.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Roadster successfully deleted.')

