import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constant import Constants

from .models import Contribution
from .forms import ContributionForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    contributions = Contribution.objects.filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(contributions))

@required_method('GET')
def show(request, contribution_id) -> JsonResponse:
    contribution = Contribution.objects.get(pk=contribution_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(contribution))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = ContributionForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Contribution successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    contribution = Contribution.objects.get(pk=content['id'])
    form = ContributionForm(instance=contribution, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form", form.errors)
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Contribution successfully updated.')

@required_method('PUT')
@csrf_protect
def activate(request, contribution_id) -> JsonResponse:
    contribution = Contribution.objects.get(pk=contribution_id)
    contribution.is_activate = not contribution.is_activate
    contribution.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Contribution successfully activated' if contribution.is_activate else 'Contribution successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, contribution_id) -> JsonResponse:
    contribution = Contribution.objects.get(pk=contribution_id)
    contribution.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Contribution successfully deleted.')

