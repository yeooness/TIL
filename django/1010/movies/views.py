from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def main(request):
    return render(request, "movies/main.html")


def index(request):
    return render(request, "movies/index.html")


def create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("movies:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "movies/create.html", context)
