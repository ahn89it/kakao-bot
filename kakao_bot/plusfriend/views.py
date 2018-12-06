from os.path import basename
import requests
from django.core.files import File
from django.shortcuts import render
from .decorators import bot
from .models import Post


@bot
def on_init(request):
    return {'type':'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']   #각 user를 식별할 수 있는 key
    type = request.JSON['type']           # type이 사진인지 글인지  구별  - audio(m4a), video(mp4)ㄹ
    content = request.JSON['content']     # 내용 - 텍스트일경우 텍스트 내용 , 사진이면 사진에 대한 URL

    if type == 'photo':
        img_url = content
        img_name = basename(img_url)
        res = requests.get(img_url, stream=True)
        post = Post(user=request.user)
        post.photo.save(img_name, File(res.raw))
        post.save()
        response = '사진을 저장했습니다.'
    else:
        post = Post.objects.create(user=request.user, message=content)
        response = ' 포스팅을 저장했습니다.'

    return {
        'message' : {
            'text' : response,
        }
    }

@bot 
def on_added(request):
    user_key = request.JSON['user_key']

@bot 
def on_block(request, user_key):
    pass

@bot 
def on_leave(request, user_key):
    pass

def post_list(request, user_key):
    qs = Post.objects.filter(user__username=user_key)
    return render(request, 'plusfriend/post_list.html', {
        'post_list' : qs,
    })