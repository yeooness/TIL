from importlib.resources import contents
import re
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    k = Review.objects.all()
    context = {"c": k}
    return render(request, "Pair1/index.html", context)


def home(request):
    k = Review.objects.all()
    return redirect("Pair1:index")


def index1(request, pk):
    k = Review.objects.all()
    return redirect("Pair1:index")


def new(request):
    return render(request, "Pair1/new.html")


def create(request):
    k = request.GET
    v = [k[i] for i in k]
    Review.objects.create(title=v[0], content=v[1])
    return redirect("Pair1:index")


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"c": k}
    return render(request, "Pair1/detail.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("Pair1:index")


def edit(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"c": k}
    return render(request, "Pair1/edit.html", context)


def update(request, pk):
    r = Review.objects.get(pk=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    r.title = title
    r.content = content

    r.save()
    return redirect("Pair1:detail", r.pk)
