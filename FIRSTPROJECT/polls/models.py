from django.db import models

# Create your models here.
# makemigrations는 application의 model에 대한 변화 기록
# migration는 makemigrations의 변화기록을 참고하여 프로젝트 모델 스키마에 반영

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # redefinition 하여 admin 페이지에 데이터 나오도록

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text