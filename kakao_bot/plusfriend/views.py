from .decorators import bot

@bot
def on_init(request):
    return {'type':'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']   #각 user를 식별할 수 있는 key
    type = request.JSON['type']           # type이 사진인지 글인지 구별 
    content = request.JSON['content']     # 내용 - 텍스트일경우 텍스트 내용 , 사진이면 사진에 대한 URL

    response = '아직 구현 되지 않음'

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
