from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.order_by("priority")
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    deadline = request.GET.get("deadline")
    priority = request.GET.get("priority")

    Todo.objects.create(
        content=content,
        created_at=created_at,
        deadline=deadline,
        priority=priority,
    )

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")
