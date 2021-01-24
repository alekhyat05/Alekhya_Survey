# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Question

from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'survey/index.html', context)

def detail(request, detail_id):
    question = get_object_or_404(Question, pk=detail_id)
    return render(request, 'survey/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)