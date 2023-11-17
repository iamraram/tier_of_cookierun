from django import forms
from board.models import Board

class PostForm(forms.ModelForm):
  class Meta:
    model = Board  # 사용할 모델
    fields = ['category', 'subject', 'description']
    