from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count

from ..forms import TipNknowhowForm
from ..models import TipNknowhow

# 팁과 노하우 글목록 출력하기
def tipNknowhow_list(request):
    '''
    shopy 팁과 노하우 글목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '') # 검색어
    sort_list = request.GET.get('sort_list', 'recent') # 글정렬
    category_local = request.GET.get('category_local', 'default_local') # 지역별 정렬
    category_sectors = request.GET.get('category_sectors', 'default_sectors') # 산업별 정렬
    tipNknowhow_list = TipNknowhow.objects.annotate(num_voter=Count('voter'), num_comment=Count('comment')).order_by('-num_voter', '-create_date') # 기본 글목록 리스트 생성

    # 지역별 카테고리 조건선택시 정렬
    local_list = ['Gangnam-gu', 'Gangdong-gu', 'Gangbuk-gu', 'Gangseo-gu', 'Gwanak-gu', 'Gwangjin-gu', 'Guro-gu', 'Geumcheon-gu', 'Geumcheon-gu', 'Nowon-gu', 'Dobong-gu', 'Dongdaemun-gu',
    'Dongjak-gu', 'Mapo-gu', 'Seodaemun-gu', 'Seocho-gu', 'Seongdong-gu', 'Songpa-gu', 'Yangcheon-gu', 'Yeongdeungpo-gu', 'Yongsan-gu', 'Eunpyeong-gu', 'Jongno-gu', 'Jung-gu', 'Jungnang-gu']

    for local in local_list:
        if category_local == local:
            tipNknowhow_list = tipNknowhow_list.filter(category_local=local).order_by('-create_date')
        else:
            tipNknowhow_list = tipNknowhow_list.order_by('-create_date')
            
    # 산업별 카테고리 조건선택시 정렬
    sector_list = ['conduct', 'marketing', 'IT', 'design', 'circulation', 'sales', 'service', 'R&D', 'production', 'erection', 'erection', 'medical', 'media', 'specialty']

    for sector in sector_list:
        if category_sectors == sector:
            tipNknowhow_list = tipNknowhow_list.filter(category_sectors=sector).order_by('-create_date')
        else:
            tipNknowhow_list = tipNknowhow_list.order_by('-create_date')

    # 글조건 선택시 정렬
    if sort_list == 'recommend':
        tipNknowhow_list = tipNknowhow_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif sort_list == 'popular':
        tipNknowhow_list = tipNknowhow_list.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:   #recent
        tipNknowhow_list = tipNknowhow_list.order_by('-create_date')

    # 검색
    if kw:
        tipNknowhow_list = tipNknowhow_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw)   # 답변 글쓴이검색
        ).distinct()
    
    # 페이징처리
    paginator = Paginator(tipNknowhow_list, 10)  # 한 페이지당 10개의 글을 페이징 객체로 변환하기.
    page_obj = paginator.get_page(page)  # paginator로 page 객체 불러오기

    context = {'tipNknowhow_list':page_obj, 'page':page, 'kw':kw, 'sort_list':sort_list, 'category_local':category_local, 'category_sectors':category_sectors}
    return render(request, 'shopy/tipNknowhow/tipNknowhow_list.html', context)


# 팁과 노하우 글 작성하기함수
@login_required(login_url='common:login')
def tipNknowhow_create(request):
    '''
    shopy 팁과 노하우 글 등록
    '''
    if request.method == 'POST':
        form = TipNknowhowForm(request.POST)
        if form.is_valid():
            tipNknowhow = form.save(commit=False)
            tipNknowhow.author = request.user
            tipNknowhow.create_date = timezone.now()
            tipNknowhow.save()
            return redirect('shopy:tipNknowhow_list')
    else:
        form = TipNknowhowForm()
    context = {'form': form}
    return render(request, 'shopy/tipNknowhow/tipNknowhow_form.html', context)

# 팁과 노하우 글 상세보기 함수
def tipNknowhow_detail(request, tipNknowhow_id):
    '''
    shopy 팁과 노하우 글 상세보기
    '''
    tipNknowhow = get_object_or_404(TipNknowhow, pk=tipNknowhow_id)
    context = {'tipNknowhow': tipNknowhow}
    return render(request, 'shopy/tipNknowhow/tipNknowhow_detail.html', context)

# 팁과 노하우 글 수정하기 함수
@login_required(login_url='common:login')
def tipNknowhow_modify(request, tipNknowhow_id):
    '''
    shopy 팁과 노하우 글 수정
    '''
    tipNknowhow = get_object_or_404(TipNknowhow, pk=tipNknowhow_id)
    
    # 작성자가 아닐경우
    if request.user != tipNknowhow.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('shopy:tipNknowhow_detail', tipNknowhow_id = tipNknowhow.id)
    
    # 작성자일 경우
    if request.method=='POST':
        form = TipNknowhowForm(request.POST, instance=tipNknowhow)
        if form.is_valid():
            tipNknowhow = form.save(commit=False)
            tipNknowhow.author = request.user
            tipNknowhow.modify_date = timezone.now()
            tipNknowhow.save()
            return redirect('shopy:tipNknowhow_detail', tipNknowhow_id = tipNknowhow.id)
    else:
        form = TipNknowhowForm(instance=tipNknowhow)
    context = {'form' : form}
    return render(request, 'shopy/tipNknowhow/tipNknowhow_form.html', context)


# 팁과 노하우 글 삭제하기 함수
@login_required(login_url='common:login')
def tipNknowhow_delete(request, tipNknowhow_id):
    '''
    shopy 팁과 노하우 글 삭제
    '''
    tipNknowhow = get_object_or_404(TipNknowhow, pk=tipNknowhow_id)
    if request.user != tipNknowhow.author:
        messages.error(request, '삭제권한이 없습니다!')
        return redirect('shopy:tipNknowhow_detail', tipNknowhow_id=tipNknowhow.id)
    tipNknowhow.delete()
    return redirect('shopy:tipNknowhow_list')