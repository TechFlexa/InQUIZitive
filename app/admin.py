from django.contrib import admin
from .models import Topic,Subtopic,Question,Answer,Attempt,Quiz,Quiz_Question

class TopicAdmin(admin.ModelAdmin):
	list_display=["topic_name"]

class SubtopicAdmin(admin.ModelAdmin):
	list_display=["subtopic_name","topic"]

class QuestionAdmin(admin.ModelAdmin):
	list_display=["question_title","question_topic","question_subtopic","question_description"]

class AnswerAdmin(admin.ModelAdmin):
	list_display=["question","answer_check","answer_score"]

class AttemptAdmin(admin.ModelAdmin):
	list_display=["attempt_user","attempt_question","attempt_score","attempt_answer","attempt_type"]

class QuizAdmin(admin.ModelAdmin):
	list_display=["quiz_title"]

class Quiz_QuestionAdmin(admin.ModelAdmin):
	list_display=["quiz","quiz_question"]



admin.site.register(Topic,TopicAdmin)
admin.site.register(Subtopic,SubtopicAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Attempt,AttemptAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Quiz_Question,Quiz_QuestionAdmin)
