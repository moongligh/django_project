from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count

from ..forms import CommunityForm
from ..models import Community

# 커뮤니티 글목록 출력하기
def community_list(request):
    '''
    shopy 커뮤니티 글목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '') # 검색어
    sort_list = request.GET.get('sort_list', 'recent') # 글정렬
    category_local = request.GET.get('category_local', 'default_local') # 지역별 정렬
    category_sectors = request.GET.get('category_sectors', 'default_local') # 산업별 정렬

    # 글정렬
    if sort_list == 'recommend':
        community_list = Community.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif sort_list == 'popular':
        community_list = Community.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:   #recent
        community_list = Community.objects.order_by('-create_date')

    # 지역별 카테고리 정렬
    if category_local == 'Gangnam-gu':
        community_list = Community.objects.filter(category_local='Gangnam-gu').order_by('-create_date')
    elif category_local == 'Gangdong-gu':
        community_list = Community.objects.filter(category_local='Gangdong-gu').order_by('-create_date')
    elif category_local == 'Gangbuk-gu':
        community_list = Community.objects.filter(category_local='Gangbuk-gu').order_by('-create_date')
    elif category_local == 'Gangseo-gu':
        community_list = Community.objects.filter(category_local='Gangseo-gu').order_by('-create_date')
    elif category_local == 'Gwanak-gu':
        community_list = Community.objects.filter(category_local='Gwanak-gu').order_by('-create_date')
    elif category_local == 'Gwangjin-gu':
        community_list = Community.objects.filter(category_local='Gwangjin-gu').order_by('-create_date')
    elif category_local == 'Guro-gu':
        community_list = Community.objects.filter(category_local='Guro-gu').order_by('-create_date')
    elif category_local == 'Geumcheon-gu':
        community_list = Community.objects.filter(category_local='Geumcheon-gu').order_by('-create_date')
    elif category_local == 'Nowon-gu':
        community_list = Community.objects.filter(category_local='Nowon-gu').order_by('-create_date')
    elif category_local == 'Dobong-gu':
        community_list = Community.objects.filter(category_local='Dobong-gu').order_by('-create_date')
    elif category_local == 'Dongdaemun-gu':
        community_list = Community.objects.filter(category_local='Dongdaemun-gu').order_by('-create_date')
    elif category_local == 'Dongjak-gu':
        community_list = Community.objects.filter(category_local='Dongjak-gu').order_by('-create_date')
    elif category_local == 'Mapo-gu':
        community_list = Community.objects.filter(category_local='Mapo-gu').order_by('-create_date')
    elif category_local == 'Seodaemun-gu':
        community_list = Community.objects.filter(category_local='Seodaemun-gu').order_by('-create_date')
    elif category_local == 'Seocho-gu':
        community_list = Community.objects.filter(category_local='Seocho-gu').order_by('-create_date')
    elif category_local == 'Seongdong-gu':
        community_list = Community.objects.filter(category_local='Seongdong-gu').order_by('-create_date')
    elif category_local == 'Seongbuk-gu':
        community_list = Community.objects.filter(category_local='Seongbuk-gu').order_by('-create_date')
    elif category_local == 'Songpa-gu':
        community_list = Community.objects.filter(category_local='Songpa-gu').order_by('-create_date')
    elif category_local == 'Yangcheon-gu':
        community_list = Community.objects.filter(category_local='Yangcheon-gu').order_by('-create_date')
    elif category_local == 'Yeongdeungpo-gu':
        community_list = Community.objects.filter(category_local='Yeongdeungpo-gu').order_by('-create_date')
    elif category_local == 'Yongsan-gu':
        community_list = Community.objects.filter(category_local='Yongsan-gu').order_by('-create_date')
    elif category_local == 'Eunpyeong-gu':
        community_list = Community.objects.filter(category_local='Eunpyeong-gu').order_by('-create_date')
    elif category_local == 'Jongno-gu':
        community_list = Community.objects.filter(category_local='Jongno-gu').order_by('-create_date')
    elif category_local == 'Jung-gu':
        community_list = Community.objects.filter(category_local='Jung-gu').order_by('-create_date')
    elif category_local == 'Jungnang-gu':
        community_list = Community.objects.filter(category_local='Jungnang-gu').order_by('-create_date')
    else: # category_local == default_local
        community_list = Community.objects.order_by('-create_date')

    
    # 산업별 카테고리 정렬
    if category_sectors == 'conduct':
        community_list = Community.objects.filter(category_sectors='conduct').order_by('-create_date')
    elif category_sectors == 'marketing':
        community_list = Community.objects.filter(category_sectors='marketing').order_by('-create_date')
    elif category_sectors == 'IT':
        community_list = Community.objects.filter(category_sectors='IT').order_by('-create_date')
    elif category_sectors == 'design':
        community_list = Community.objects.filter(category_sectors='design').order_by('-create_date')
    elif category_sectors == 'circulation':
        community_list = Community.objects.filter(category_sectors='circulation').order_by('-create_date')
    elif category_sectors == 'sales':
        community_list = Community.objects.filter(category_sectors='salesu').order_by('-create_date')
    elif category_sectors == 'service':
        community_list = Community.objects.filter(category_sectors='service').order_by('-create_date')
    elif category_sectors == 'R&D':
        community_list = Community.objects.filter(category_sectors='R&D').order_by('-create_date')
    elif category_sectors == 'production':
        community_list = Community.objects.filter(category_sectors='production').order_by('-create_date')
    elif category_sectors == 'education':
        community_list = Community.objects.filter(category_sectors='education').order_by('-create_date')
    elif category_sectors == 'erection':
        community_list = Community.objects.filter(category_sectors='erection').order_by('-create_date')
    elif category_sectors == 'medical':
        community_list = Community.objects.filter(category_sectors='medical').order_by('-create_date')
    elif category_sectors == 'media':
        community_list = Community.objects.filter(category_sectors='media').order_by('-create_date')
    elif category_sectors == 'specialty':
        community_list = Community.objects.filter(category_sectors='specialty').order_by('-create_date')
    else: # category_sectors == default_sectors
        community_list = Community.objects.order_by('-create_date')

    # 검색
    if kw:
        community_list = community_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw) |  # 답변 글쓴이검색
            Q(category_local__icontains=kw) | # 글작성 카테고리(지역)
            Q(category_sectors__icontains=kw) # 글작성 카테고리(산업)
        ).distinct()

    # 페이징처리
    paginator = Paginator(community_list, 10)  # 한 페이지당 10개의 글을 페이징 객체로 변환하기.
    page_obj = paginator.get_page(page)  # paginator로 page 객체 불러오기

    context = {'community_list':page_obj, 'page':page, 'kw':kw, 'sort_list':sort_list, 'category_local':category_local, 'category_sectors':category_sectors}
    return render(request, 'shopy/community/community_list.html', context)


# 커뮤니티 글 작성하기함수
@login_required(login_url='common:login')
def community_create(request):
    '''
    shopy 커뮤니티 글 등록
    '''
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.author = request.user
            community.create_date = timezone.now()
            community.save()
            return redirect('shopy:community_list')
    else:
        form = CommunityForm()
    context = {'form': form}
    return render(request, 'shopy/community/community_form.html', context)

# 커뮤니티 글 상세보기 함수
def community_detail(request, community_id):
    '''
    shopy 커뮤니티 글 상세보기
    '''
    community = get_object_or_404(Community, pk=community_id)
    context = {'community': community}
    return render(request, 'shop/community/community_detail.html', context)

# 커뮤니티 글 수정하기 함수
@login_required(login_url='common:login')
def community_modify(request, community_id):
    '''
    shopy 커뮤니티 글 수정
    '''
    community = get_object_or_404(Community, pk=community_id)
    
    # 작성자가 아닐경우
    if request.user != community.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('shopy:community_detail', community_id = community.id)
    
    # 작성자일 경우
    if request.method=='POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            community = form.save(commit=False)
            community.author = request.user
            community.category_local = request.category_local
            community.category_sectors = request.category_sectors
            community.modify_date = timezone.now()
            community.save()
            return redirect('shopy:community_detail', community_id = community.id)
    else:
        form = CommunityForm(instance=community)
    context = {'form' : form}
    return render(request, 'shopy/community/community_form.html', context)


# 커뮤니티 글 삭제하기 함수
@login_required(login_url='common:login')
def community_delete(request, community_id):
    '''
    shopy 커뮤니티 글 삭제
    '''
    community = get_object_or_404(Community, pk=community)
    if request.user != community.author:
        messages.error(request, '삭제권한이 없습니다!')
        return redirect('shopy:community_detail', community_id=community.id)
    community.delete()
    return redirect('shopy:community_list')