from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .utils import fail, success


class CustomJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if response := renderer_context.get('response'):
            response: Response
            if response.status_code in range(200, 400):
                data = success(data)
            else:
                data = fail(data)
        return super().render(data, accepted_media_type, renderer_context)
