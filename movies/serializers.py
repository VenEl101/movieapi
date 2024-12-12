from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movies.models import Actor, Movie, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'birthdate', 'gender')

    def validate_source(self, value):
        if not value > '01.01.1950':
            raise ValidationError('Birthdate must be greater than 01.01.1950')
        
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'movie_id', 'text', 'created_at') 



    

