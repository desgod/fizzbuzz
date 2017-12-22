from rest_framework import serializers
from fizzbuzz.api.models import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message',)
        read_only_fields = ('fizzbuzz_id', 'useragent', 'creation_date',)

    def create(self, validated_data):
        request = self.context.get("request")
        useragent = request.META['HTTP_USER_AGENT']

        return FizzBuzz.objects.create(message=validated_data['message'], useragent=useragent)

