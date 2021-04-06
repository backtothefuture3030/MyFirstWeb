from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True) #blank=True는 form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미이다.
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가
    def __str__(self):   # cmd창에서 사람이 알아볼수있도록 표현하기위해서
        return self.subject




class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미이다.
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True) # blank=True는 form.is_valid()를 통한 입력 폼 데이터 검사 시 값이 없어도 된다는 의미이다.
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

