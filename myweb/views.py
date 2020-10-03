from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request,'myweb/index.html')

def contract(request):
    return render(request,'myweb/contract.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/sign_up.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')

#def detail(request, question_id):
   # return render(request, 'myweb/detail.html')

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)

#def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)