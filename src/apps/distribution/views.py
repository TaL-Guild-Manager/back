import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constants import Constants

from .models import Distribution
from .forms import DistributionForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    distributions = Distribution.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(distributions))

@required_method('GET')
def show(request, distribution_id) -> JsonResponse:
    distribution = Distribution.objects.get(pk=distribution_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(distribution))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = DistributionForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Distribution successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    distribution = Distribution.objects.get(pk=content['id'])
    form = DistributionForm(instance=distribution, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Distribution successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, distribution_id) -> JsonResponse:
    distribution = Distribution.objects.get(pk=distribution_id)
    distribution.is_activate = not distribution.is_activate
    distribution.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Distribution successfully activated' if distribution.is_activate else 'Distribution successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, distribution_id) -> JsonResponse:
    distribution = Distribution.objects.get(pk=distribution_id)
    distribution.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Distribution successfully deleted.')

