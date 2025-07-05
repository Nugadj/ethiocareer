from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exams_home(request):
    return render(request, 'exams_main.html')
