from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "movie_name", "content", "grade"]
        labels = {
            "title": "리뷰 제목",
            "movie_name": "영화 제목",
            "content": "리뷰 내용",
            "grade": "평점",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
