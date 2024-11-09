import django_filters
from django_filters import FilterSet, ModelChoiceFilter, CharFilter
from .models import Author
from django import forms


class PostFilter(FilterSet):
    heading = CharFilter(
        label='Заголовок',
        lookup_expr='iregex')

    author = ModelChoiceFilter(
        empty_label='Все авторы',
        label='Авторы',
        queryset=Author.objects.all())

    time_create = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte')
