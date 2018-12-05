from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def bot(views_fn):
    @wraps(views_fn)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            request.JSON = json.loads(request.body.decode('utf8'))
        else:
            request.JSON = {}
        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap