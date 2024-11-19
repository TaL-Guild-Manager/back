import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest, ObjectDoesNotExist

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constants import Constants

from .models import BiS
from .forms import BiSForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    biss = BiS.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(biss))

@required_method('GET')
def show(request, bis_id) -> JsonResponse:
    bis = BiS.objects.get(pk=bis_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(bis))

def find(request) -> JsonResponse:
    bis = BiS.objects.filter(member__username__icontains=request.GET.get('username', None).lower()).first()

    if not bis:
        raise ObjectDoesNotExist("No BiS found with this username")

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(bis))


@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = BiSForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'BiS successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    bis = BiS.objects.get(pk=content['id'])
    form = BiSForm(instance=bis, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'BiS successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, bis_id) -> JsonResponse:
    bis = BiS.objects.get(pk=bis_id)
    bis.is_activate = not bis.is_activate
    bis.save()

    return api_response(HttpCode.SUCCESS, 'success', 'BiS successfully activated' if bis.is_activate else 'BiS successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, bis_id) -> JsonResponse:
    bis = BiS.objects.get(pk=bis_id)
    bis.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'BiS successfully deleted.')

