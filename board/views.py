from django.shortcuts import render, get_object_or_404
from .models import Board

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