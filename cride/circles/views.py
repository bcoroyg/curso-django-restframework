"""Circles views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from cride.circles.models import Circle

# Serializers
from cride.circles.serializers import (
    CircleSerializer,
    CreateCircleSerializer
)


@api_view(['GET'])
def list_circles(request):
    """List circles."""
    circles = Circle.objects.filter(is_public=True)

    """
    data = []
    for circle in circles:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit,
        })
    return Response(data)
    """

    """
    data = []
    for circle in circles:
        serializer = CircleSerializer(circle)
        data.append(serializer.data)
    return Response(data)
    """

    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_circle(request):
    """Create circle."""

    """
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data = {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'rides_taken': circle.rides_taken,
        'rides_offered': circle.rides_offered,
        'members_limit': circle.members_limit,
    }
    return Response(data)
    """

    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # data = serializer.data
    # circle = Circle.objects.create(**data)
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)
