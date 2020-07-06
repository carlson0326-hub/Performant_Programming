from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'home.html', {'quizzes': quizzes})
