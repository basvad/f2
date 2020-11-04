from django.contrib import admin

# Register your models here.

from p_pols.models import Question, Choice, UserProfile,Poll,Answer

#регистрация модели варианта ответа
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

#регистрация модели вопроса
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]
    search_fields = ['title']


#регистрация модели опроса
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'publish')
    raw_id_fields = ("question",)
    list_filter = ['pub_date']
    search_fields = ['title']
admin.site.register(Poll, PollAdmin)


#регистрация модели пользователя
@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass

#регистрация модели ответа
@admin.register(Answer)  
class ProfileAdmin(admin.ModelAdmin):  
    list_display = ('user', 'poll', 'question','choice','created')
    search_fields = ['user','poll']
