from rest_framework import serializers
from shorturl.models import UrlShort, UserAgent

class AgentSerializers(serializers.Serializer):
    ''' (serializers.ModelSerializer)
        class Meta:
            model = UserAgent
            fields = ('user_agent','user_national', 'start', 'end')
    '''
    agent = serializers.CharField(max_length=100)
    nation = serializers.CharField(max_length=50)
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    def validate(self, data):
        if data['start'] > data['end']:
            raise serializers.ValidationError('date start must be small than date end')
        return data
