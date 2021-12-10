from django import template
from django.db.models import Count
from ..models import Portfolio
from comment.models import Comment

register = template.Library()


@register.simple_tag
def total_portfolios():
    return Portfolio.objects.count()


@register.simple_tag
def total_comments():
    return Comment.objects.count()
