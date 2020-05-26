# 사용자 정의 필터
from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg