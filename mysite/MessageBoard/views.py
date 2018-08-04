from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import User, Board, Agree, Comment
from django.db import models
import json
from django.http import JsonResponse
from django.core import serializers

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
        board = Board(UID_id = int(request.GET.get('UID')), title = request.GET.get('title'), message = request.GET.get('message'))
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
    MID = int(request.GET.get('MID'))
    UID = int(request.GET.get('UID'))
    try:
        if Agree.objects.filter(UID_id = UID, MID_id = MID).exists():
            Agree.objects.filter(UID_id = UID, MID_id = MID).update(agree = request.GET.get('agree'))
        else:
            agree = Agree(UID_id = UID, MID_id = MID, agree = request.GET.get('agree'))
            agree.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)

@require_http_methods(['GET'])
def add_comment(request):
    response = {}
    try:
        comment = Comment(MID_id = int(request.GET.get('MID')), UID_id = int(request.GET.get('UID')), comment = request.GET.get('comment'))
        comment.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)

@require_http_methods(['GET'])
def get_UID(request):
    response = {}
    username = request.GET.get('username')
    password = request.GET.get('password')
    try:
        # response['password'] = json.loads(serializers.serialize('json', User.objects.all()))
        response['UID'] = User.objects.get(username = username, password = password).UID
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(['GET'])
def get_board(request):
    MID = int(request.GET.get('MID'))
    response = {}
    try:
        board = Board.objects.get(MID = MID)
        response['message'] = board.message
        response['title'] = board.title
        response['UID'] = board.UID_id
        response['time'] = board.time
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)

@require_http_methods(['GET'])
def get_username(request):
    UID = int(request.GET.get('UID'))
    response = {}
    try:
        user = User.objects.get(UID = UID)
        response['username'] = user.username
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(['GET'])
def get_agreeNumber(request):
    MID = int(request.GET.get('MID'))
    response = {}
    try:
        agreeNumber = Agree.objects.filter(MID_id = MID, agree = True).count()
        response['agreeNumber'] = agreeNumber
        response['error_num'] = 0
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(['GET'])
def get_disagreeNumber(request):
    MID = int(request.GET.get('MID'))
    response = {}
    try:
        disagreeNumber = Agree.objects.filter(MID_id = MID, agree = False).count()
        response['disagreeNumber'] = disagreeNumber
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)

@require_http_methods(['GET'])
def get_amAgree(request):
    MID = request.GET.get('MID')
    UID = request.GET.get('UID')
    response = {}
    try:
        if Agree.objects.get(MID_id = MID, UID_id = UID).agree == True:
            response['amAgree'] = 1
        else:
            response['amAgree'] = -1
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = 'success'
        response['error_num'] = 0
        response['amAgree'] = 0

    return JsonResponse(response)

@require_http_methods(['GET'])
def get_comments(request):
    MID = request.GET.get('MID')
    response = {}
    try:
        comments = Comment.objects.filter(MID_id = MID).all()
        response['list'] = json.loads(serializers.serialize('json', comments))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(['GET'])
def get_totalNumber(request):
    response = {}
    try:
        total = Board.objects.all().count()
        response['total'] = total
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    
    return JsonResponse(response)
        