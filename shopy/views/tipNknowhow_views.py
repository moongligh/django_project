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

    # 글정렬
    if sort_list == 'recommend':
        tipNknowhow_list = TipNknowhow.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif sort_list == 'popular':
        tipNknowhow_list = TipNknowhow.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:   #recent
        tipNknowhow_list = TipNknowhow.objects.order_by('-create_date')
    
    # 지역별 카테고리 정렬
    if category_local == 'Gangnam-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gangnam-gu').order_by('-create_date')
    elif category_local == 'Gangdong-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gangdong-gu').order_by('-create_date')
    elif category_local == 'Gangbuk-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gangbuk-gu').order_by('-create_date')
    elif category_local == 'Gangseo-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gangseo-gu').order_by('-create_date')
    elif category_local == 'Gwanak-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gwanak-gu').order_by('-create_date')
    elif category_local == 'Gwangjin-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Gwangjin-gu').order_by('-create_date')
    elif category_local == 'Guro-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Guro-gu').order_by('-create_date')
    elif category_local == 'Geumcheon-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Geumcheon-gu').order_by('-create_date')
    elif category_local == 'Nowon-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Nowon-gu').order_by('-create_date')
    elif category_local == 'Dobong-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Dobong-gu').order_by('-create_date')
    elif category_local == 'Dongdaemun-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Dongdaemun-gu').order_by('-create_date')
    elif category_local == 'Dongjak-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Dongjak-gu').order_by('-create_date')
    elif category_local == 'Mapo-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Mapo-gu').order_by('-create_date')
    elif category_local == 'Seodaemun-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Seodaemun-gu').order_by('-create_date')
    elif category_local == 'Seocho-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Seocho-gu').order_by('-create_date')
    elif category_local == 'Seongdong-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Seongdong-gu').order_by('-create_date')
    elif category_local == 'Seongbuk-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Seongbuk-gu').order_by('-create_date')
    elif category_local == 'Songpa-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Songpa-gu').order_by('-create_date')
    elif category_local == 'Yangcheon-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Yangcheon-gu').order_by('-create_date')
    elif category_local == 'Yeongdeungpo-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Yeongdeungpo-gu').order_by('-create_date')
    elif category_local == 'Yongsan-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Yongsan-gu').order_by('-create_date')
    elif category_local == 'Eunpyeong-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Eunpyeong-gu').order_by('-create_date')
    elif category_local == 'Jongno-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Jongno-gu').order_by('-create_date')
    elif category_local == 'Jung-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Jung-gu').order_by('-create_date')
    elif category_local == 'Jungnang-gu':
        tipNknowhow_list = TipNknowhow.objects.filter(category_local='Jungnang-gu').order_by('-create_date')
    else: # category_local == default_local
        tipNknowhow_list = TipNknowhow.objects.order_by('-create_date')
    
    # 산업별 카테고리 정렬
    if category_sectors == 'conduct':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='conduct').order_by('-create_date')
    elif category_sectors == 'marketing':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='marketing').order_by('-create_date')
    elif category_sectors == 'IT':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='IT').order_by('-create_date')
    elif category_sectors == 'design':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='design').order_by('-create_date')
    elif category_sectors == 'circulation':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='circulation').order_by('-create_date')
    elif category_sectors == 'sales':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='salesu').order_by('-create_date')
    elif category_sectors == 'service':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='service').order_by('-create_date')
    elif category_sectors == 'R&D':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='R&D').order_by('-create_date')
    elif category_sectors == 'production':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='production').order_by('-create_date')
    elif category_sectors == 'education':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='education').order_by('-create_date')
    elif category_sectors == 'erection':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='erection').order_by('-create_date')
    elif category_sectors == 'medical':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='medical').order_by('-create_date')
    elif category_sectors == 'media':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='media').order_by('-create_date')
    elif category_sectors == 'specialty':
        tipNknowhow_list = TipNknowhow.objects.filter(category_sectors='specialty').order_by('-create_date')
    else: # category_sectors == default_sectors
        tipNknowhow_list = TipNknowhow.objects.order_by('-create_date')

    # 검색
    if kw:
        tipNknowhow_list = tipNknowhow_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw) |  # 답변 글쓴이검색
            Q(category_local__icontains=kw) | # 글작성 카테고리(지역)
            Q(category_sectors__icontains=kw) # 글작성 카테고리(산업)
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