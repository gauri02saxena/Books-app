from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Book
from ..serializers import BookSerializer
import django_filters

class BookFilter(django_filters.FilterSet):
    """
    Basic field-level filtering for Book model (used in GET query param filtering).
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    pages = django_filters.NumberFilter(field_name='pages', lookup_expr='gt')
    author__city = django_filters.CharFilter(field_name='author__city', lookup_expr='iexact')

    class Meta:
        model = Book
        fields = ['title', 'pages', 'author__city']

def build_query(node):
    """
    Builds a Django Q object from nested or flat filter payloads.

    Supports:
    - Nested: { "operator": "and" | "or", "children": [ ... ] }
    - Flat: { "field": ..., "op": ..., "value": ... }

    Returns:
    - Combined Q object
    """
    if isinstance(node, dict):
        if "operator" in node and "children" in node:
            op = node["operator"].lower()
            children = node["children"]
            if not isinstance(children, list):
                raise ValueError("'children' must be a list")

            q = Q()
            for child in children:
                sub_q = build_query(child)
                if op == "and":
                    q &= sub_q
                elif op == "or":
                    q |= sub_q
                else:
                    raise ValueError(f"Invalid operator: {op}")
            return q

        elif all(k in node for k in ("field", "op", "value")):
            return Q(**{f"{node['field']}__{node['op']}": node["value"]})

    raise ValueError("Invalid filter structure")

class BookDynamicFilterView(APIView):
    """
    Handles complex, nested filtering of Book data via POST request.
    Payload supports logical nesting with 'and'/'or' and multiple field conditions.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            filters = request.data
            q_object = build_query(filters)
            queryset = Book.objects.filter(q_object).distinct()
            serializer = BookSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
