from rest_framework import serializers

from fizzbuzz.api.models import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
    """
    FizzBuzz Serializer
    """
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message',)
        read_only_fields = ('fizzbuzz_id', 'useragent', 'creation_date',)

    def create(self, validated_data):
        """
        This method creates a new FizzBuzz object using the message data sent and pulling the useragent
        from the request meta data 
        
        :param validated_data: Validated data from the POST request 
        :return: a newly created FizzBuzz object
        """
        request = self.context.get("request")
        useragent = request.META.get('HTTP_USER_AGENT', 'N/A')

        return FizzBuzz.objects.create(message=validated_data['message'], useragent=useragent)

