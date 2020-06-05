from django.urls import path
from .views import base_views, community_views, QNA_views, tipNknowhow_views, comment_views, vote_views

app_name = 'shopy'

urlpatterns = [

    # base_views.py
    path('', base_views.home, name='home'),
    path('our_local_is/', base_views.our_local_is, name='our_local_is'),

    # community_views.py
    path('community/list/', community_views.community_list, name='community_list'),
    path('community/create/', community_views.community_create, name='community_create'),
    path('community/detail/<int:community_id>/', community_views.community_detail, name='community_detail'),
    path('community/modify/<int:community_id>/', community_views.community_modify, name='community_modify'),
    path('community/delete/<int:community_id>/', community_views.community_delete, name='community_delete'),

    # QNA_views.py
    path('QNA/list/', QNA_views.QNA_list, name='QNA_list'),
    path('QNA/create/', QNA_views.QNA_create, name='QNA_create'),
    path('QNA/detail/<int:QnA_id>/', QNA_views.QNA_detail, name='QNA_detail'),
    path('QNA/modify/<int:QnA_id>/', QNA_views.QNA_modify, name='QNA_modify'),
    path('QNA/delete/<int:QnA_id>/', QNA_views.QNA_delete, name='QNA_delete'),

    # tipNknowhow_views.py
    path('tipNknowhow/list/', tipNknowhow_views.tipNknowhow_list, name='tipNknowhow_list'),
    path('tipNknowhow/create/', tipNknowhow_views.tipNknowhow_create, name='tipNknowhow_create'),
    path('tipNknowhow/detail<int:tipNknowhow_id>/', tipNknowhow_views.tipNknowhow_detail, name='tipNknowhow_detail'),
    path('tipNknowhow/modify/<int:tipNknowhow_id>/', tipNknowhow_views.tipNknowhow_modify, name='tipNknowhow_modify'),
    path('tipNknowhow/delete/<int:tipNknowhow_id>/', tipNknowhow_views.tipNknowhow_delete, name='tipNknowhow_delete'),

    # comment_views.py
        # 커뮤니티 댓글
    path('comment/create/community/<int:community_id>/', comment_views.comment_create_community, name='comment_create_community'),
    path('comment/modify/community/<int:comment_id>/', comment_views.comment_modify_community, name='comment_modify_community'),
    path('comment/delete/community/<int:comment_id>/', comment_views.comment_delete_community, name='comment_delete_community'),
        # QNA 댓글
    path('comment/create/QNA/<int:QnA_id>/', comment_views.comment_create_QNA, name='comment_create_QNA'),
    path('comment/modify/QNA/<int:comment_id>/', comment_views.comment_modify_QNA, name='comment_modify_QNA'),
    path('comment/delete/QNA/<int:comment_id>/', comment_views.comment_delete_QNA, name='comment_delete_QNA'),
        # 팁과 노하우 댓글
    path('comment/create/tipNknowhow/<int:tipNknowhow_id>/', comment_views.comment_create_tipNknowhow, name='comment_create_tipNknowhow'),
    path('comment/modify/tipNknowhow/<int:comment_id>/', comment_views.comment_modify_tipNknowhow, name='comment_modify_tipNknowhow'),
    path('comment/delete/tipNknowhow/<int:comment_id>/', comment_views.comment_delete_tipNknowhow, name='comment_delete_tipNknowhow'),

    # vote_views.py (게시글 추천)
    path('vote/community/<int:community_id>/', vote_views.vote_community, name='vote_community'),
    path('vote/QNA/<int:QnA_id>/', vote_views.vote_QNA, name='vote_QNA'),
    path('vote/tipNknowhow/<int:tipNknowhow_id>/', vote_views.vote_tipNknowhow, name='vote_tipNknowhow'),
]
