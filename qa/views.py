from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from qa.models import Question

import random

def index(request):
    question_list = Question.objects.all()
    question = question_list[random.randrange(len(question_list))]
    answer_list = question.answer_set.all()
    answer = answer_list[random.randrange(len(answer_list))]
    context = {'question': question, 'answer':answer}
    return render(request, 'qa/index.html', context)

