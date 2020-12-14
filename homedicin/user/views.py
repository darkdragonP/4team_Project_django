from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_protect
from user.models import *

from buisness.models import md_Board, select_md_board, delete_md_board, update_md_board, insert_md_board, detile_md_board

# Create your views here.

def home(request):

    medicine = getDetail(request.GET.get('MD_CODE'))
    medicine = getDetail(medicine)

    medicine2 = getDetail2(request.GET.get('MD_CODE'))
    medicine2 = getDetail2(medicine2)

    search1 = search_ingr(request.GET.get('MD_CODE'))
    search1 = search_ingr(search1)

    search2 = search_effect(request.GET.get('MD_CODE'))
    search2 = search_effect(search2)



    return render(request, 'user/index.html',{'getDetail2': medicine2,'getDetail':medicine,'search_ingr':search1,'search_effect':search2})

def home2(request):

    medicine = getDetail(request.GET.get('MD_CODE'))
    medicine = getDetail(medicine)

    medicine2 = getDetail2(request.GET.get('MD_CODE'))
    medicine2 = getDetail2(medicine2)

    search1 = search_ingr(request.GET.get('MD_CODE'))
    search1 = search_ingr(search1)

    search2 = search_effect(request.GET.get('MD_CODE'))
    search2 = search_effect(search2)


    return render(request, 'user/2.html',{'getDetail2': medicine2,'getDetail':medicine,'search_ingr':search1,'search_effect':search2})

def home3(request):

    medicine = getDetail(request.GET.get('MD_CODE'))
    medicine = getDetail(medicine)

    medicine2 = getDetail2(request.GET.get('MD_CODE'))
    medicine2 = getDetail2(medicine2)

    search1 = search_ingr(request.GET.get('MD_CODE'))
    search1 = search_ingr(search1)

    search2 = search_effect(request.GET.get('MD_CODE'))
    search2 = search_effect(search2)


    return render(request, 'user/3.html',{'getDetail2': medicine2,'getDetail':medicine,'search_ingr':search1,'search_effect':search2})

def home2_1(request):

    medicine = getDetail(request.GET.get('MD_CODE'))
    medicine = getDetail(medicine)

    medicine2_1 = getDetail2_1(request.GET.get('MD_CODE'))
    medicine2_1 = getDetail2_1(medicine2_1)

    search1 = search_ingr(request.GET.get('MD_CODE'))
    search1 = search_ingr(search1)

    search2 = search_effect(request.GET.get('MD_CODE'))
    search2 = search_effect(search2)


    return render(request, 'user/2_1.html',{'getDetail2_1': medicine2_1,'getDetail':medicine,'search_ingr':search1,'search_effect':search2})

def home3_1(request):

    medicine = getDetail(request.GET.get('MD_CODE'))
    medicine = getDetail(medicine)

    medicine2_1 = getDetail2_1(request.GET.get('MD_CODE'))
    medicine2_1 = getDetail2_1(medicine2_1)

    search1 = search_ingr(request.GET.get('MD_CODE'))
    search1 = search_ingr(search1)

    search2 = search_effect(request.GET.get('MD_CODE'))
    search2 = search_effect(search2)


    return render(request, 'user/3_1.html',{'getDetail2_1': medicine2_1,'getDetail':medicine,'search_ingr':search1,'search_effect':search2})
