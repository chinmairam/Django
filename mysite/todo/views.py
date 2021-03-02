from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
# Create your views here.


def todoView(request):
    all_items = Todo.objects.all()
    return render(request, 'todo.html', {'all_items': all_items})
    # return HttpResponse("Hello, This is todoView")


def addTodo(request):
    new_item = Todo(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = Todo.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
