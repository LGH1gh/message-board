from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import User, Board, Agree, Comment
from django.db import models
from django.http import JsonResponse

# Create your views here.
@require_http_methods(['GET'])
def add_user(request):
    response = {}
    username = request.GET.get('username')
    if User.objects.filter(username = username).exists():
        response['msg'] = 'The name has been used'
        response['error_num'] = -1
    else:
        try:
            user = User(username = username, password = request.GET.get('password'))
            user.save()
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1

        return JsonResponse(response)


@require_http_methods(['GET'])
def add_board(request):
    response = {}
    try:
        board = Board(UID = request.GET.get('UID'), title = request.GET.get('title'), message = request.GET.get('message'))
        board.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(['GET'])
def add_agree(request):
    response = {}
    MID = request.GET.get('MID')
    UID = request.GET.get('UID')
    try:
        if Agree.objects.filter(UID = UID, MID = MID).exists():
            Agree.objects.filter(UID = UID, MID = MID).update(agree = request.GET.get('agree'))
        else:
            agree = Agree(UID = UID, MID = MID, agree = request.GET.get('agree'))
            agree.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

@require_http_methods(['GET'])
def add_comment(request):
    response = {}
    try:
        comment = Comment(MID = request.GET.get('MID'), UID = request.GET.get('UID'), comment = request.GET.get('comment'))
        comment.save()
        response['msg'] = 'success'
        response['error_code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1