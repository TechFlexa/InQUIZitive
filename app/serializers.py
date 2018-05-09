from rest_framework import models
from rest_framework import serializers
from .models import UserProfile,Topic,Subtopic,Question,Answer,Attempt,Quiz,Quiz_Question
from django.contrib.auth.models import User

class StockSerializer1(serializers.ModelSerializer):

      class Meta:
            model = User
            fields = '__all__'


class StockSerializer2(serializers.ModelSerializer):

      class Meta:
            model = UserProfile
            fields = '__all__' 


class StockSerializer3(serializers.ModelSerializer):

      class Meta:
            model = Topic
            fields = '__all__' 

class StockSerializer4(serializers.ModelSerializer):

      class Meta:
            model = Subtopic
            fields = '__all__' 

class StockSerializer5(serializers.ModelSerializer):

      class Meta:
            model = Question
            fields = '__all__' 

class StockSerializer6(serializers.ModelSerializer):

      class Meta:
            model = Answer
            fields = '__all__' 

class StockSerializer7(serializers.ModelSerializer):

      class Meta:
            model = Attempt
            fields = '__all__' 

class StockSerializer8(serializers.ModelSerializer):

      class Meta:
            model = Quiz
            fields = '__all__' 

class StockSerializer9(serializers.ModelSerializer):

      class Meta:
            model = Quiz_Question
            fields = '__all__' 