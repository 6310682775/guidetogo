import django_filters
from django_filters import LookupChoiceFilter
from tour.models import *
from django import forms

class Tourfilter(django_filters.FilterSet):
    price = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices = [
            ('exact', 'Equals'),
            ('gt', 'Greater than'),
            ('lt', 'Less than'),
        ]
    )
    period = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices = [
            ('exact', 'Equals'),
            ('gt', 'Greater than'),
            ('lt', 'Less than'),
        ]
    )
    amount = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices = [
            ('exact', 'Equals'),
            ('gt', 'Greater than'),
            ('lt', 'Less than'),
        ]
    )

    avg_rating = django_filters.LookupChoiceFilter(
        field_class=forms.DecimalField,
        lookup_choices = [
            ('exact', 'Equals'),
            ('gt', 'Greater than'),
            ('lt', 'Less than'),
        ]
    )
    
    class Meta:     
        model = Tour
        fields = {
                'province': ['icontains'],
                'price':['exact'], 
                'period':['exact'],  
                'amount':['exact'],
                'avg_rating':['exact'],
                }
        