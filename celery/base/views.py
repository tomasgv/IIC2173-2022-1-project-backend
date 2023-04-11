# django
from django.views.generic import TemplateView

# tasks
from base.tasks import wait_and_return, calc_indices

from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["POST"])
def welcome(request):
    result = calc_indices.delay(request.data["id_ping"])
    content = {"message": "Task started", "task_id": result.id}
    return JsonResponse(content)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        return 'Hello World'

class WaitView(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        wait_and_return.delay()
        return super().get(self, *args, **kwargs)
