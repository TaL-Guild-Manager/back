import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import FieldError, BadRequest

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants
from src.decorators.request_method_validator import required_method

from .models import Grade
from .forms import GradeForm
from .serializers import list_serializer, show_serializer

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    grades = Grade.objects.all().values().filter(is_activate=filter)

    return api_response(HttpCode.SUCCESS, 'success', data=list_serializer(grades))

@required_method('GET')
def show(request, grade_id) -> JsonResponse:
    grade = Grade.objects.get(pk=grade_id)

    return api_response(HttpCode.SUCCESS, 'success', data=show_serializer(grade))

@required_method('POST')
@csrf_protect
def add(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    form = GradeForm(content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.CREATED, 'success', 'Grade successfully created.')

@required_method('PATCH')
@csrf_protect
def update(request) -> JsonResponse:
    if not request.body:
        raise BadRequest("Body request is missing")
    
    content = json.loads(request.body.decode('utf-8'))
    grade = Grade.objects.get(pk=content['id'])
    form = GradeForm(instance=grade, data=content)

    if not form.is_valid():
        raise FieldError("Invalid form")
    
    form.save()
    return api_response(HttpCode.SUCCESS, 'success', 'Grade successfully updated.')


@required_method('PUT')
@csrf_protect
def activate(request, grade_id) -> JsonResponse:
    grade = Grade.objects.get(pk=grade_id)
    grade.is_activate = not grade.is_activate
    grade.save()

    return api_response(HttpCode.SUCCESS, 'success', 'Grade successfully activated.' if grade.is_activate else 'Grade successfully deactivated.')

@required_method('DELETE')
@csrf_protect
def delete(request, grade_id) -> JsonResponse:
    grade = Grade.objects.get(pk=grade_id)
    grade.delete()

    return api_response(HttpCode.SUCCESS, 'success', 'Grade successfully deleted.')