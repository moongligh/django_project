from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count

from ..forms import QNAForm
from ..models import QNA

# QNA 글목록 출력하기
def QNA_list(request):
    '''
    shopy QNA 글목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '') # 검색어
    sort_list = request.GET.get('sort_list', 'recent') # 글정렬
    category_local = request.GET.get('category_local', 'default_local') # 지역별 카테고리
    category_sectors = request.GET.get('category_sectors', 'default_sectors') # 산업별 카테고리

    # 글정렬
    if sort_list == 'recommend':
        QnA_list = QNA.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif sort_list == 'popular':
        QnA_list = QNA.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:   #recent
        QnA_list = QNA.objects.order_by('-create_date')

    # 지역별 카테고리 정렬
    if category_local == 'Gangnam-gu':
        QnA_list = QNA.objects.filter(category_local='Gangnam-gu').order_by('-create_date')
    elif category_local == 'Gangdong-gu':
        QnA_list = QNA.objects.filter(category_local='Gangdong-gu').order_by('-create_date')
    elif category_local == 'Gangbuk-gu':
        QnA_list = QNA.objects.filter(category_local='Gangbuk-gu').order_by('-create_date')
    elif category_local == 'Gangseo-gu':
        QnA_list = QNA.objects.filter(category_local='Gangseo-gu').order_by('-create_date')
    elif category_local == 'Gwanak-gu':
        QnA_list = QNA.objects.filter(category_local='Gwanak-gu').order_by('-create_date')
    elif category_local == 'Gwangjin-gu':
        QnA_list = QNA.objects.filter(category_local='Gwangjin-gu').order_by('-create_date')
    elif category_local == 'Guro-gu':
        QnA_list = QNA.objects.filter(category_local='Guro-gu').order_by('-create_date')
    elif category_local == 'Geumcheon-gu':
        QnA_list = QNA.objects.filter(category_local='Geumcheon-gu').order_by('-create_date')
    elif category_local == 'Nowon-gu':
        QnA_list = QNA.objects.filter(category_local='Nowon-gu').order_by('-create_date')
    elif category_local == 'Dobong-gu':
        QnA_list = QNA.objects.filter(category_local='Dobong-gu').order_by('-create_date')
    elif category_local == 'Dongdaemun-gu':
        QnA_list = QNA.objects.filter(category_local='Dongdaemun-gu').order_by('-create_date')
    elif category_local == 'Dongjak-gu':
        QnA_list = QNA.objects.filter(category_local='Dongjak-gu').order_by('-create_date')
    elif category_local == 'Mapo-gu':
        QnA_list = QNA.objects.filter(category_local='Mapo-gu').order_by('-create_date')
    elif category_local == 'Seodaemun-gu':
        QnA_list = QNA.objects.filter(category_local='Seodaemun-gu').order_by('-create_date')
    elif category_local == 'Seocho-gu':
        QnA_list = QNA.objects.filter(category_local='Seocho-gu').order_by('-create_date')
    elif category_local == 'Seongdong-gu':
        QnA_list = QNA.objects.filter(category_local='Seongdong-gu').order_by('-create_date')
    elif category_local == 'Seongbuk-gu':
        QnA_list = QNA.objects.filter(category_local='Seongbuk-gu').order_by('-create_date')
    elif category_local == 'Songpa-gu':
        QnA_list = QNA.objects.filter(category_local='Songpa-gu').order_by('-create_date')
    elif category_local == 'Yangcheon-gu':
        QnA_list = QNA.objects.filter(category_local='Yangcheon-gu').order_by('-create_date')
    elif category_local == 'Yeongdeungpo-gu':
        QnA_list = QNA.objects.filter(category_local='Yeongdeungpo-gu').order_by('-create_date')
    elif category_local == 'Yongsan-gu':
        QnA_list = QNA.objects.filter(category_local='Yongsan-gu').order_by('-create_date')
    elif category_local == 'Eunpyeong-gu':
        QnA_list = QNA.objects.filter(category_local='Eunpyeong-gu').order_by('-create_date')
    elif category_local == 'Jongno-gu':
        QnA_list = QNA.objects.filter(category_local='Jongno-gu').order_by('-create_date')
    elif category_local == 'Jung-gu':
        QnA_list = QNA.objects.filter(category_local='Jung-gu').order_by('-create_date')
    elif category_local == 'Jungnang-gu':
        QnA_list = QNA.objects.filter(category_local='Jungnang-gu').order_by('-create_date')
    else: # category_local == default_local
        QnA_list = QNA.objects.order_by('-create_date')

    
    # 산업별 카테고리 정렬
    if category_sectors == 'conduct':
        QnA_list = QNA.objects.filter(category_sectors='conduct').order_by('-create_date')
    elif category_sectors == 'marketing':
        QnA_list = QNA.objects.filter(category_sectors='marketing').order_by('-create_date')
    elif category_sectors == 'IT':
        QnA_list = QNA.objects.filter(category_sectors='IT').order_by('-create_date')
    elif category_sectors == 'design':
        QnA_list = QNA.objects.filter(category_sectors='design').order_by('-create_date')
    elif category_sectors == 'circulation':
        QnA_list = QNA.objects.filter(category_sectors='circulation').order_by('-create_date')
    elif category_sectors == 'sales':
        QnA_list = QNA.objects.filter(category_sectors='salesu').order_by('-create_date')
    elif category_sectors == 'service':
        QnA_list = QNA.objects.filter(category_sectors='service').order_by('-create_date')
    elif category_sectors == 'R&D':
        QnA_list = QNA.objects.filter(category_sectors='R&D').order_by('-create_date')
    elif category_sectors == 'production':
        QnA_list = QNA.objects.filter(category_sectors='production').order_by('-create_date')
    elif category_sectors == 'education':
        QnA_list = QNA.objects.filter(category_sectors='education').order_by('-create_date')
    elif category_sectors == 'erection':
        QnA_list = QNA.objects.filter(category_sectors='erection').order_by('-create_date')
    elif category_sectors == 'medical':
        QnA_list = QNA.objects.filter(category_sectors='medical').order_by('-create_date')
    elif category_sectors == 'media':
        QnA_list = QNA.objects.filter(category_sectors='media').order_by('-create_date')
    elif category_sectors == 'specialty':
        QnA_list = QNA.objects.filter(category_sectors='specialty').order_by('-create_date')
    else: # category_sectors == default_sectors
        QnA_list = QNA.objects.order_by('-create_date')

    # 검색
    if kw:
        QnA_list = QnA_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(QnA_list, 10)  # 한 페이지당 10개의 글을 페이징 객체로 변환하기.
    page_obj = paginator.get_page(page)  # paginator로 page 객체 불러오기

    context = {'QnA_list':page_obj, 'page':page, 'kw':kw, 'sort_list':sort_list, 'category_local':category_local, 'category_sectors':category_sectors}
    return render(request, 'shopy/QNA/QNA_list.html', context)


# QNA 글 작성하기함수
@login_required(login_url='common:login')
def QNA_create(request):
    '''
    shopy QNA 글 등록
    '''
    if request.method == 'POST':
        form = QNAForm(request.POST)
        if form.is_valid():
            QnA = form.save(commit=False)
            QnA.author = request.user
            QnA.create_date = timezone.now()
            QnA.save()
            return redirect('shopy:QNA_list')
    else:
        form = QNAForm()
    context = {'form': form}
    return render(request, 'shopy/QNA/QNA_form.html', context)

# QNA 글 상세보기 함수
def QNA_detail(request, QnA_id):
    '''
    shopy QNA 글 상세보기
    '''
    QnA = get_object_or_404(QNA, pk=QnA_id)
    context = {'QnA': QnA}
    return render(request, 'shopy/QNA/QNA_detail.html', context)

# QNA 글 수정하기 함수
@login_required(login_url='common:login')
def QNA_modify(request, QnA_id):
    '''
    shopy QNA 글 수정
    '''
    QnA = get_object_or_404(QNA, pk=QnA_id)
    
    # 작성자가 아닐경우
    if request.user != QnA.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('shopy:QNA_detail', QnA_id = QnA.id)
    
    # 작성자일 경우
    if request.method=='POST':
        form = QNAForm(request.POST, instance=QnA)
        if form.is_valid():
            QnA = form.save(commit=False)
            QnA.author = request.user
            QnA.modify_date = timezone.now()
            QnA.save()
            return redirect('shopy:QNA_detail', QnA_id = QnA.id)
    else:
        form = QNAForm(instance=QnA)
    context = {'form' : form}
    return render(request, 'shopy/QNA/QNA_form.html', context)

# QNA 글 삭제하기 함수
@login_required(login_url='common:login')
def QNA_delete(request, QnA_id):
    '''
    shopy QNA 글 삭제
    '''
    QnA = get_object_or_404(QNA, pk=QnA_id)
    if request.user != QnA.author:
        messages.error(request, '삭제권한이 없습니다!')
        return redirect('shopy:QNA_detail', QnA_id=QnA.id)
    QnA.delete()
    return redirect('shopy:QNA_list')