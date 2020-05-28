from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Community, QNA, TipNknowhow

# 커뮤니티글 추천 함수
@login_required(login_url='common:login')
def vote_community(request, community_id):
    '''
    shopy 커뮤니티글 추천등록
    '''
    community = get_object_or_404(Community, pk=community_id)
    if request.user == community.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        community.voter.add(request.user)
    return redirect('shopy:community_detail', community_id=community.id)

# QNA글 추천 함수
@login_required(login_url='common:login')
def vote_QNA(request, QnA_id):
    '''
    shopy QNA글 추천등록
    '''
    QnA = get_object_or_404(QNA, pk=QnA_id)
    if request.user == QnA.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        QnA.voter.add(request.user)
    return redirect('shopy:QNA_detail', QnA_id=QnA.id)

# 팁과 노하우글 추천 함수
@login_required(login_url='common:login')
def vote_tipNknowhow(request, tipNknowhow_id):
    '''
    shopy 팁과 노하우글 추천등록
    '''
    tipNknowhow = get_object_or_404(TipNknowhow, pk=tipNknowhow_id)
    if request.user == tipNknowhow.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        tipNknowhow.voter.add(request.user)
    return redirect('shopy:tipNknowhow_detail', tipNknowhow_id=tipNknowhow.id)