from rest_framework import serializers
from dictionary.models import Word

class ShortWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'title', 'definition', 'language')


class WordSerializer(serializers.ModelSerializer):
    
    translation = ShortWordSerializer(many=True)

    class Meta:
        model = Word
        fields = ('id', 'title', 'definition', 'language', 'translation', 'synonyms', 'antonyms')
