"""
    Service to return pre-formatted JsonResponse API
"""
import logging
import os

from django.http import JsonResponse
from src.contracts.constant import Constants
# from .webhook import Webhook

logger = logging.getLogger(__name__)
http_codes = Constants.HttpResponseCodes


def send_json_response(code=http_codes.SUCCESS, result='success', message='', data=None, url='', user='', payload=None) -> JsonResponse:
    """
    Send response in JSON format. The response is returned with code, result and data.

    Args:
        code (Constants.HttpResponseCode, optional): Response status code. Defaults to 'SUCCESS'.
        result (str, optional): Response message. Defaults to 'success'
        message (str, optional): Message to display. Defaults to ''
        data (dict, optional): Response data. Defaults to {}.
        url (str, optional): url where the error has occurred
        user (str, optional): the user that received the error
        payload (object, optional): the payload that was sent
    Returns:
        JsonResponse with the code, the result, the message and the data
    """

    if data is None:
        data = []

    # if code.value >= 400 and os.getenv("ENV") == "prod":
    #     logger.error("Received error %s with the following message: %s", code.value, message)
    #     Webhook.discord(code=code, message=message, url=url, user=user, payload=payload, data=data)

    return JsonResponse({
        'code': code.value,
        'result': result,
        'message': message,
        'data': data
    })