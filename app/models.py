from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone as django_tz 
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class Topic(models.Model):
	topic_name=models.CharField(max_length=50)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
	      return self.topic_name

class Subtopic(models.Model):
	topic=models.ForeignKey(Topic)
	subtopic_name=models.CharField(max_length=50)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
		return self.subtopic_name

class Question(models.Model):
	question_topic=models.ForeignKey(Topic)
	question_subtopic=models.ForeignKey(Subtopic)
	question_title=models.CharField(max_length=1000)
	question_description=models.CharField(max_length=10000)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
		return self.question_title

class Answer(models.Model):
	question=models.ForeignKey(Question)
	answer_check = models.BooleanField(default=True)
	answer_score=models.FloatField(default=0.0)
	answer_description=models.CharField(max_length=10000)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
		return self.answer_description

class Attempt(models.Model):
	Attempt_choices = (
	(1,'Practice',),
	(2,'Quiz',),
	)
	attempt_user=models.ForeignKey(User)
	attempt_question=models.ForeignKey(Question)
	attempt_score=models.FloatField(default=0.0)
	attempt_answer=models.CharField(max_length=1000)
	attempt_type=models.IntegerField(choices=Attempt_choices)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
		return self.attempt_answer

class Quiz(models.Model):
	quiz_title=models.CharField(max_length=100)
	quiz_description=models.CharField(max_length=10000)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)
	def __str__(self):
		return self.quiz_title

class Quiz_Question(models.Model):
	quiz=models.ForeignKey(Quiz)
	quiz_question=models.ForeignKey(Question)
	created_at = models.DateTimeField(default=django_tz.now)
	updated_at = models.DateTimeField(default=django_tz.now)


class UserProfile(models.Model):
	user = models.OneToOneField(User,blank=False)
	mobile=PhoneNumberField()
	def __unicode__(self):
		return self.user.username

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	        UserProfile.objects.create(user=instance)





