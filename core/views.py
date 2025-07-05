from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')
@login_required(login_url='/login/')
def exams(request):
    return render(request, 'exams.html')
@login_required(login_url='/login/')
def quiz(request):
    return render(request, 'quiz.html')
@login_required(login_url='/login/')
def pay(request):
    return render(request, 'pay.html')
@login_required(login_url='/login/')
def scholarships(request):
    return render(request, 'scholarships.html')
@login_required(login_url='/login/')
def jobs(request):
    return render(request, 'jobs.html')
@login_required(login_url='/login/')
def job_exams(request):
    return render(request, 'job-exams.html')
@login_required(login_url='/login/')
def job_ethiopian_airlines(request):
    return render(request, 'job-ethiopian-airlines.html')
@login_required(login_url='/login/')
def job_ethio_telecom(request):
    return render(request, 'job-ethio-telecom.html')
@login_required(login_url='/login/')
def job_insa(request):
    return render(request, 'job-insa.html')
@login_required(login_url='/login/')
def grade12_exams(request):
    return render(request, 'grade12-exams.html')
@login_required(login_url='/login/')
def grade12_natural(request):
    return render(request, 'grade12-natural.html')
@login_required(login_url='/login/')
def grade12_social(request):
    return render(request, 'grade12-social.html')
@login_required(login_url='/login/')
def physics_exams(request):
    return render(request, 'physics-exams.html')
@login_required(login_url='/login/')
def chemistry_exams(request):
    return render(request, 'chemistry-exams.html')
@login_required(login_url='/login/')
def biology_exams(request):
    return render(request, 'biology-exams.html')
@login_required(login_url='/login/')
def math_exams(request):
    return render(request, 'math-exams.html')
@login_required(login_url='/login/')
def civics_exams(request):
    return render(request, 'civics-exams.html')
@login_required(login_url='/login/')
def history_exams(request):
    return render(request, 'history-exams.html')
@login_required(login_url='/login/')
def geography_exams(request):
    return render(request, 'geography-exams.html')
@login_required(login_url='/login/')
def economics_exams(request):
    return render(request, 'economics-exams.html')
@login_required(login_url='/login/')
def ict_exams(request):
    return render(request, 'ict-exams.html')
@login_required(login_url='/login/')
def logic_exams(request):
    return render(request, 'logic-exams.html')
@login_required(login_url='/login/')
def university_exams(request):
    return render(request, 'university-exams.html')
@login_required(login_url='/login/')
def astu_courses(request):
    return render(request, 'astu-courses.html')
@login_required(login_url='/login/')
def astu_appliedmath1(request):
    return render(request, 'astu-appliedmath1.html')
@login_required(login_url='/login/')
def aastu_courses(request):
    return render(request, 'aastu_courses.html')
@login_required(login_url='/login/')
def aau_courses(request):
    return render(request, 'aau_courses.html')
@login_required(login_url='/login/')
def astu_appliedmath1_final(request):
    return render(request, 'astu_appliedmath1_final.html')
@login_required(login_url='/login/')
def astu_appliedmath1_mid(request):
    return render(request, 'astu_appliedmath1_mid.html')
@login_required(login_url='/login/')
def astu_appliedmath1_outline(request):
    return render(request, 'astu_appliedmath1_outline.html')
@login_required(login_url='/login/')
def astu_appliedmath1_resources(request):
    return render(request, 'astu_appliedmath1_resources.html')
@login_required(login_url='/login/')
def astu_chemistry(request):
    return render(request, 'astu_chemistry.html')
@login_required(login_url='/login/')
def astu_electrical(request):
    return render(request, 'astu_electrical.html')
@login_required(login_url='/login/')
def astu_physics1(request):
    return render(request, 'astu_physics1.html')
@login_required(login_url='/login/')
def astu_programming(request):
    return render(request, 'astu_programming.html')
@login_required(login_url='/login/')
def ethio_network_engineer_exams(request):
    return render(request, 'ethio_network_engineer_exams.html')
@login_required(login_url='/login/')
def physics_2024(request):
    return render(request, 'physics_2024.html')

@login_required(login_url='/login/')
def job_civil_service(request):
    return render(request, 'job_civil_service.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # ✅ Saves to database
            auth_login(request, user)  # ✅ Logs in after register
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})