from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from user.models import CustomUser

def board_read(request):
    boards = Board.objects.all()
    context = {'boards' : boards}
    return render(request, 'board/read.html', context)

def board_read_one(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/read_one.html', {'board':board})

def board_create(request):
    if request.method == 'POST' and request.session.get('user', False):
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username=request.session['user'])
        content = request.POST['content']
        board = Board(
            author = author,
            title = title,
            content = content
            )
        board.save()
        return redirect('board_read')
    else:
        return render(request, 'board/create.html')

def board_update(request,pk):
    title = request.POST['title'] 
    author = get_object_or_404(CustomUser, username=request.session['user'])
    content = request.POST['content']
    board = Board.objects.get(pk=pk)
    board.author = author
    board.title = title
    board.content = content
    board.save()
    return redirect('board_read')

def pre_update(request,pk):
    board = Board.objects.get(pk = pk)
    context = {'board': board}
    return render(request, 'board/update.html', context)

def board_delete(request,pk):
    board = Board.objects.get(pk = pk)
    board.delete()
    return redirect('board_read')