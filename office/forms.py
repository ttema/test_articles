from django import forms
from .models import Article, TimePeriod


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


class TimePeriodForm(forms.ModelForm):

    class Meta:
        model = TimePeriod
        fields = ('start_date', 'end_date', 'description')
        labels = {
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'description': 'НАзвание события'
        }
