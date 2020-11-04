from django.shortcuts import render,get_object_or_404
from p_pols.models import Question, Choice, Poll, Answer,UserProfile
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import auth  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy,reverse

from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

# Create your views here.

def questions_list(request):
    question = Question.objects.all()
    return HttpResponse(question)

class QuestionList(ListView):
    model = Question
    template_name = 'question_list.html'

#главную страницу

#страница тестов
@login_required
def index(request):  
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username  
    return render(request, 'test.html', context)

#страница опросов
@login_required
def poll(request):  
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        #получаем профайл пользователя
        profile = get_object_or_404(UserProfile, user=request.user)
        ##получить все ответы пользователя по БД 
        answers = Answer.objects.all().filter(user=profile)
        #лист пройденных опросов
        finish_polls_list = []
        for i in answers:
            if i.poll.id not in finish_polls_list:
                finish_polls_list.append(i.poll.id)
        print(finish_polls_list)
        #получаем доступные опросы
        polls = Poll.objects.all().filter(pub_date__lt=timezone.now())
        # формируем лист ожидания опросов
        start_polls_list = []
        for j in polls:
            if j.id not in finish_polls_list:
                start_polls_list.append(j)
        context['polls'] = start_polls_list
    return render(request, 'poll.html', context)


#страница статистики
@login_required
def stat(request):  
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        #получаем профайл пользователя
        profile = get_object_or_404(UserProfile, user=request.user)
        ##получить все ответы пользователя по БД 
        answers = Answer.objects.all().filter(user=profile)
        context['answers']=answers
    return render(request, 'stat.html', context)

#детали опроса
@login_required
def detail(request, poll_id):
    #return HttpResponse("Вы смотрите на опрос %s." % poll_id)
    context = {} 
    context['username'] = request.user.username 
    #получаем профайл пользователя
    profile = get_object_or_404(UserProfile, user=request.user)
    try:
        poll = Poll.objects.get(pk=poll_id)
        context['poll']=poll
        question_list=[]
        for i in poll.question.all():
            question_list.append(i.id)
        context['question_list']=question_list
    except Poll.DoesNotExist:
        raise Http404
    #проверка существования
    if Answer.objects.all().filter(user=profile).filter(poll=poll).exists():
        return HttpResponseRedirect(reverse('common:results', args=(poll_id,)))
    else:
        return render(request, 'detail.html', context)
    #return render(request, 'detail.html', context)
#результаты
@login_required
def results(request, poll_id):
    context = {} 
    context['username'] = request.user.username
    #получаем профайл пользователя
    profile = get_object_or_404(UserProfile, user=request.user)
    #получаем текущий опрос 
    r_poll = get_object_or_404(Poll,pk=poll_id)
    context['poll']=r_poll
    #получаем ответы пользователя
    context['user_answers'] = Answer.objects.all().filter(user=profile).filter(poll=r_poll)
    #response = "Вы смотрите на результаты опроса %s."
    #return HttpResponse(response % poll_id)
    return render(request, 'results.html', context)

import json

#голос
@login_required
def vote(request, poll_id):
    #return HttpResponse("Вы голосуете по опросу %s." % poll_id)
    #получаем профайл пользователя
    profile = get_object_or_404(UserProfile, user=request.user)
    for key,value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            #получаем опрос 
            result_poll = get_object_or_404(Poll,pk=poll_id)
            #получаем опрос
            result_question = get_object_or_404(Question,pk=key)
            #получаем вариант
            result_choice = get_object_or_404(Choice,pk=value)
            #сохраняем в БД
            #проверка существования
            if Answer.objects.all().filter(user=profile).filter(poll=result_poll).filter(choice=result_choice).exists():
               pass
            else:
                result = Answer(user=profile, poll=result_poll, question=result_question,choice=result_choice)
                result.save()
            #print ('{}->{}'.format(key,value))
    #json_list = json.dumps(request.POST)
    #return HttpResponse("Вы голосуете по опросу %s." % json_list)
    return HttpResponseRedirect(reverse('common:results', args=(poll_id,)))