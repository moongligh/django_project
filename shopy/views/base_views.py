from django.core.paginator import Paginator
from django.shortcuts import render

def home(request):
    '''
    Shopy 메인 홈페이지 이동
    '''
    return render(request, 'shopy/home.html', {})