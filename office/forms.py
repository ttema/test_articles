from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'prev', 'text', 'photo')
        labels = {
            'title': 'Название',
            'prev': 'Аннотация',
            'text': 'Содержание',
            'photo': 'Обложка'
        }
