from django.shortcuts import render
from .models import logininfo


def homepage(request):
    return render(request, 'login.html')


def login(request):
    # fname = request.GET['fullname']
    # mail = request.GET['loginid']
    # passwd = request.GET['password']
    return render(request, 'login_success.html')


def login_info_admin(request):
    fullname = request.POST['fullname']
    loginid = request.POST['loginid']
    pw = request.POST['passid']

    faculty_info = logininfo(name=fullname, email=loginid, password=pw)
    faculty_info.save()

    return render(request, 'login_success.html')
