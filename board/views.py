from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board
from django.http import HttpResponse 

from .forms import PostForm

def index(request):
  board_list = Board.objects.order_by('-create_date')
  context = {'board_list': board_list}
  return render(request, 'board/board_list.html', context)

def detail(request, question_id):
  board_detail = get_object_or_404(Board, pk=question_id)
  context = {'board_detail': board_detail}
  return render(request, 'board/board_detail.html', context)

def notfound(request, exception):
  return render(request, 'not_found.html', status=404)


def board_write(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      question = form.save(commit=False)
      question.create_date = timezone.now()
      question.comment = '[]'
      question.view = 0
      question.save()
      return redirect('/board')
    
  else:
    form = PostForm()
    context = {'form': form}
    return render(request, 'board/board_write.html', context)
