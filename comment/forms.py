from django import forms
from .models import Comment


class PortfolioCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
