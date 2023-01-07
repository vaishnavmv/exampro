from django.contrib import messages

from django.contrib.auth import authenticate, login


from django.shortcuts import render, redirect


# Create your views here.
from demoapp1.forms import LoginForm, TrainerForm


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('home')
            elif user.is_trainer:
                return redirect('trainer_home')
            elif user.is_user:
                return redirect('student_home')
            else:
                messages.info(request,'invalid credential')
    return render(request, 'login_view.html')

def trainer_register(request):
        login_form = LoginForm()
        trainer_form = TrainerForm()
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            trainer_form = TrainerForm(request.POST, request.FILES)
            if login_form.is_valid() and trainer_form.is_valid():
                user = login_form.save(commit=False)
                user.is_trainer = True
                user.save()
                trainer = trainer_form.save(commit=False)
                trainer.user = user
                trainer.save()
                messages.info(request, 'Registration successfully')
                return redirect('trainer_view')
        return render(request, 'trainer_register.html',
                      {'login_form': login_form, 'trainer_form': trainer_form})

