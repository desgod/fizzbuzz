from rest_framework import viewsets, mixins
from fizzbuzz.api.models import FizzBuzz
from fizzbuzz.api.serializers import FizzBuzzSerializer


class FizzBuzzViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    Fizz Buzz API endpoint
    """
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer


