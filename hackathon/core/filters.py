import django_filters
from .models import *

class AwareFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        field_name='description', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['description']