# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import leaves

# Create your views here.

def homepage(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            attended = []
            unattended = []
            for each in reversed(leaves.objects.all()):
                if(each.status == 'u'):
                    unattended.append(each)
                else:
                    attended.append(each)
            return render(request,'registration/home_admin.html',{'attended': attended,'unattended' : unattended})
        else:
            dic = leaves.objects.filter(user = request.user).all()
            return render(request,'registration/home_emp.html',{'leaves': reversed(dic)})
    else:
        return render(request,'registration/home.html')


def request_leave(request):
    if(request.method == 'POST' and request.user.is_authenticated and not request.user.is_superuser):
        leave = leaves()
        leave.user = request.user
        leave.desc = request.POST["description"]
        leave.fromdate = request.POST["from"]
        leave.todate = request.POST["to"]
        leave.status = 'u'
        leave.save()
        return redirect('./')
    else:
        return redirect('./')



def respond_leave(request):
    if(request.method == 'POST' and request.user.is_authenticated and request.user.is_superuser):
        leave = leaves.objects.filter(id = int(request.POST["which"])).first()
        leave.status = request.POST["what"]
        leave.save()
        return redirect('./')
    else:
        return redirect('./')