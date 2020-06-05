from django.core.paginator import Paginator
from django.shortcuts import render

def home(request):
    '''
    Shopy 메인 홈페이지 이동
    '''
    return render(request, 'shopy/home.html', {})

# '우리지역은?' 출력
def our_local_is(request):
    '''
    shopy 우리지역은? 페이지로 이동
    '''
    return render(request, 'shopy/Our_Local_Is/our_local_is.html', {})