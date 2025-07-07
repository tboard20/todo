from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request,"home.html")

def index(request):
    return render(request, "index.html")

# def login(request):
#     return render(request,"registration/login.html")

# def logout(request):
#     return render(request,"registration/logout.html")

def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('task_list')
    else:
            form =UserCreationForm()


    return render(request,"registration/signup.html",{'form': form})
    
