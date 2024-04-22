from django.template.response import SimpleTemplateResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response as DRFResponse
from core.api.api_responses import APIResponse

class CustomAPIResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Check if the response is a TemplateResponse (or a subclass)
        if isinstance(response, SimpleTemplateResponse):
            # Render the response
            response.render()
            data = response.content
        # Check if the response is a DRF Response
        elif isinstance(response, DRFResponse):
            data = response.data
        else:
            data = response.content

        # Wrap the content data in the APIResponse format
        if response.status_code < 400:
            return APIResponse('success', data=data)
        else:
            return APIResponse('error', data=data)