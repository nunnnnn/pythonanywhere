from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#from .form import *
#from .models import Farm,Vegetable,Season

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


#--------DB----#



def showVegetable(testrequestreq):
    vegetable = Vegetable.objects.all()
    return render(testrequestreq ,'myweb/allvegetable.html' ,{'vegetable':vegetable})

def addfarm(req):
    if req.method == "POST":
        form = addFarm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addFarm()
        context = {'form':form}
        return render(req, 'myweb/add.html',context)

def addvegetable(req):
    if req.method == "POST":
        form = addVegetable(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addVegetable()
        context = {'form':form}
        return render(req, 'myweb/add.html',context)


def search(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            searchby = form.cleaned_data['SearchBy']
            keyword = form.cleaned_data['keyword']
            if searchby == '1':
                vegetables = Vegetable.objects.filter(Vegetable_Name__contains=keyword)
            elif searchby == '2':
                try:

                    keyword = float(keyword)

                except:

                    form = SearchForm()
                    context = {'form':form}
                    return render(req, 'myweb/search.html',context)
                vegetables = Vegetables.objects.filter(Price=keyword)
                
            elif searchby == '3':
                vegetables = Vegetable.objects.filter(Season__SeasonName__contains=keyword)
            elif searchby == '4':
                vegetables = Vegetables.objects.filter(FarmName__Farm_Name__contains=keyword)
            return render(req , "myweb/showvegetable.html",{"vegetables":vegetables})
    else:
        form = SearchForm()
        context = {'form':form}
        return render(req, 'myweb/search.html',context)