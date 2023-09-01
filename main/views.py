from django.http import JsonResponse
from django.shortcuts import render,redirect

import utils

def signup(request):
    if request.method == 'GET':
        return render(request,"signup.html")
    elif request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        db=utils.Connect_To_DB()
        collection=db["user"]
        data={
            "name":name,
            "email":email,
            "password":password,
        }
        collection.insert_one(data)
        return redirect("/all/")
        
        
def Home(request):
    return render(request,"all.html")

def signin(request):
    return render(request,"signin.html")

def create(request):
    return render(request,'create.html')