from rest_framework import serializers
from quiz.models import QuizUser, Quiz


class QuizUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizUser
        fields = ('user', 'quiz', 'score')


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('name', 'description', 'created')



