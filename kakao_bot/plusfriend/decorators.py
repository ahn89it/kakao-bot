from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json

User = get_user_model()

def bot(view_fn):
    @wraps(view_fn)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            request.JSON = json.loads(request.body.decode('utf8'))
        else:
            request.JSON = {}
        
        user_key = request.JSON.get('user_key')           #user_key를 request로 가져오기
        user_key = kwargs.get('user_key', user_key)       #user_key를 kwargs로 가져오기 
        if user_key:       
            username = 'kakao-' + user_key                              
            try:                                              #user_key가 있다면
                request.user = User.objects.get(username=username)            
            except User.DoesNotExist:                        #user_key 없다면
                request.user = User.objects.create_user(username=username)

        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap