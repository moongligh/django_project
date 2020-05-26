from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Community, QNA, TipNknowhow

# 커뮤니티글 댓글 작성하기 함수
@login_required(login_url='common:login')
def comment_create_community(request, community_id):
    '''
    shopy 커뮤니티글의 댓글작성
    '''
    community = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.community = community
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:community_detail', community_id = comment.community.id), community.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'shopy/comment/community_comment.html', context)


# 질문글 댓글 수정하기 함수
@login_required(login_url='common:login')
def comment_modify_community(request, comment_id):
    '''
    shopy 커뮤니티글의 댓글수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다!')
        return redirect('shopy:community_detail', community_id = comment.community.id)

    # 댓글작성자인데, 전송방식이 'POST'방식일 경우
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:community_detail', community_id=comment.community.id), community.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'shopy/comment/community_comment.html', context)


# 질문글 댓글 삭제하기 함수
@login_required(login_url='common:login')
def comment_delete_community(request, comment_id):
    '''
    shopy 커뮤니티글의 댓글삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다!')
        return redirect('shopy:community_detail', community_id = comment.community.id)
    
    # 댓글 작성자일 경우
    else:
        comment.delete()
    return redirect('shopy:community_comment', community_id = comment.community.id)

# QNA글 댓글 작성하기 함수
@login_required(login_url='common:login')
def comment_create_QNA(request, QnA_id):
    '''
    shopy QNA글의 댓글작성
    '''
    QnA = get_object_or_404(QNA, pk=QnA_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.QnA = QnA
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:QnA_detail', QnA_id = comment.QnA.id), QnA.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'shopy/comment/QNA_comment.html', context)


# QNA글 댓글 수정하기 함수
@login_required(login_url='common:login')
def comment_modify_QNA(request, comment_id):
    '''
    shopy QNA글의 댓글수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다!')
        return redirect('shopy:QNA_detail', QnA_id = comment.QnA.id)

    # 댓글작성자인데, 전송방식이 'POST'방식일 경우
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:QNA_detail', QnA_id=comment.QnA.id), QnA.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'shopy/comment/QNA_comment.html', context)


# 질문글 댓글 삭제하기 함수
@login_required(login_url='common:login')
def comment_delete_QNA(request, comment_id):
    '''
    shopy QNA의 댓글삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다!')
        return redirect('shopy:QNA_detail', QnA_id = comment.QnA.id)
    
    # 댓글 작성자일 경우
    else:
        comment.delete()
    return redirect('shopy:QNA_comment', QnA_id = comment.QnA.id)

# 팁과 노하우글 댓글 작성하기 함수
@login_required(login_url='common:login')
def comment_create_tipNknowhow(request, tipNknowhow_id):
    '''
    shopy 팁과 노하우글의 댓글작성
    '''
    tipNknowhow = get_object_or_404(TipNknowhow, pk=tipNknowhow_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.tipNknowhow = tipNknowhow
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:tipNknowhow_detail', tipNknowhow_id = comment.tipNknowhow.id), tipNknowhow.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'shopy/comment/tipNknowhow_comment.html', context)


# 질문글 댓글 수정하기 함수
@login_required(login_url='common:login')
def comment_modify_tipNknowhow(request, comment_id):
    '''
    shopy 팁과 노하우글의 댓글수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다!')
        return redirect('shopy:tipNknowhow_detail', tipNknowhow_id = comment.tipNknowhow.id)

    # 댓글작성자인데, 전송방식이 'POST'방식일 경우
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('shopy:tipNknowhow_detail', tipNknowhow_id=comment.tipNknowhow.id), tipNknowhow.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'shopy/comment/tipNknowhow_comment.html', context)


# 질문글 댓글 삭제하기 함수
@login_required(login_url='common:login')
def comment_delete_tipNknowhow(request, comment_id):
    '''
    shopy 커뮤니티글의 댓글삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다!')
        return redirect('shopy:tipNknowhow_detail', tipNknowhow_id = comment.tipNknowhow.id)
    
    # 댓글 작성자일 경우
    else:
        comment.delete()
    return redirect('shopy:tipNknowhow_comment', tipNknowhow_id = comment.tipNknowhow.id)