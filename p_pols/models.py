from django.db import models
from django.contrib.auth.models import User  
import datetime
from django.utils import timezone


#модель пользователя
class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
           return self.user.username


# модель вопросов
class Question(models.Model):
    title = models.CharField(max_length=4096,  help_text="Вопрос", verbose_name="Вопрос")
    def __str__(self):
           return self.title

#модель опроса
class Poll(models.Model):
    title = models.CharField(max_length=4096,  help_text="Опрос", verbose_name="Опрос")
    question = models.ManyToManyField(Question, related_name='polls',help_text="Вопрос", verbose_name="Вопрос")
    pub_date = models.DateTimeField(help_text="Дата публикации", verbose_name="Дата публикации",default=timezone.now())
    def publish(self):
        return self.pub_date <= timezone.now()
    publish.admin_order_field = 'pub_date'
    publish.boolean = True
    publish.short_description = 'Опубликовано ?'
    def __str__(self):
           return self.title

#модель вариантов ответов к вопросам
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=4096, help_text="Вариант ответа", verbose_name="Вариант ответа")
    def __str__(self):
        return self.title



#модель ответов пользователя
class Answer(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, default=None)
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, default=None)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.poll.title
