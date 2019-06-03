from django.shortcuts import render
from .models import registrationData
from .forms import registrationform,loginform
from django.http.response import HttpResponse

# Create your views here.
def reg_view(request):
    if request.method == "POST":
        rform = registrationform(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            mobile = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            data = registrationData(first_name=first_name,
                                  last_name = last_name,
                                  username = username,
                                  password = password,
                                  mobile = mobile,
                                  email = email)
            data.save()
            lform=loginform()
            return render(request,'login_form.html',{'lform':lform})
        else:
            return HttpResponse("invalid data")
    else:
        rform=registrationform()
        return render (request,'reg_form.html',{'rform':rform})
def login_view(request):
    if request.method=="POST":
        lform=loginform(request.POST)
        if lform.is_valid():
            username = request.POST.get('username', ' ')
            password = request.POST.get('password', ' ')
            uname1 = registrationData.objects.filter( username=username)
            pwd1 = registrationData.objects.filter(password=password)
            if uname1 and pwd1:
                return HttpResponse("correct username and password")
            else:
                return HttpResponse("wrong username and password")
        else:
            return HttpResponse("invalid data")

    else:
        lform = loginform()
        return render(request, 'login_form.html', {'lform': lform})


