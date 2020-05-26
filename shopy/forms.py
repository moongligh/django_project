from django import forms  # 장고의 기본 폼형식
from shopy.models import Community, QNA, TipNknowhow, Comment
# 모델 폼, 연결된 모델의 데이터를 저장할 수 있게된다. Class Meta라는 내부클래스가 필수이다.


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['subject', 'content', 'category_local', 'category_sectors']
        labels = {
            'subject': '제목',
            'content': '내용',
            'category_local': '지역별 카테고리',
            'category_sectors': '산업별 카테코리', 
        }


class QNAForm(forms.ModelForm):
    class Meta:
        model = QNA
        fields = ['subject', 'content', 'category_local', 'category_sectors']
        labels = {
            'subject': '제목',
            'content': '내용',
            'category_local': '지역별 카테고리',
            'category_sectors': '산업별 카테코리', 
        }

class TipNknowhowForm(forms.ModelForm):
    class Meta:
        model = TipNknowhow
        fields = ['subject', 'content', 'category_local', 'category_sectors']
        labels = {
            'subject': '제목',
            'content': '내용',
            'category_local': '지역별 카테고리',
            'category_sectors': '산업별 카테코리', 
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }