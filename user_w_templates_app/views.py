from django.shortcuts import render, redirect
from .models import *  

def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'index.html', context)

def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        age=request.POST['age'],
    )
    return redirect('/')
    
# echo "# users_w_templates" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/users_w_templates.git
# git push -u origin main