from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'prev', 'text',)
        labels = {
            'title': 'Название',
            'prev': 'Аннотация',
            'text': 'Содержание'
        }
