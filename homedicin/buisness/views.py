from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from buisness.models import md_Board, select_md_board, delete_md_board, update_md_board, insert_md_board, detile_md_board

# Create your views here.

def home(request):
    md_Board()
    return render(request, 'buisness/index.html')


def select_ad_board(request):
    idx = request.GET["idx"]
    msg_board = select_md_board(idx)
    return render(request, 'buisness/list.html', {'msg':msg_board})

def detile_ad_board(request):
    idx = request.GET["idx"]
    msg_board = detile_md_board(idx)
    return render(request, 'buisness/detail.html', {'msg':msg_board})

@csrf_protect
def insert_ad_board(request):
    ad_borad = (request.POST['user_code'], request.POST['admin_board_title'], request.POST['admin_board_contents'])
    print('data :', ad_borad)
    insert_md_board(ad_borad)
    return render(request, 'buisness/list.html')

@csrf_protect
def update_ad_borad(request):
    ad_borad = (request.POST['admin_board_title'], request.POST['admin_board_contents'])
    print('data :', ad_borad)
    insert_md_board(ad_borad)
    return render(request, 'buisness/list.html')