from django.http import HttpResponse
from HR.functions import handle_uploaded_file
from HR.forms import ApplicantResume
from django.shortcuts import render
from .models import HR_Registration,Applicant_Registration,Manager_Registration,Interviewer_Registration



# Create your views here.
def showhome(request):
    type = request.GET.get('type')
    return render(request,'index.html',{'type':type})

def Hrlogin(request):
    type = request.GET.get('type')
    return render(request,'index.html',{'type':type})



def HRsignup(request):
    name =request.POST.get('name')
    company_name =request.POST.get('company_name')
    username =request.POST.get('username')
    password =request.POST.get('password')
    repassword =request.POST.get('repassword')
    type ='hr_login'

    if password == repassword:
        HRRegistration = HR_Registration(name=name,company_name=company_name,password=password,email=username)
        HRRegistration.save()
        return render(request,'index.html',{'type':type})
    else:
        return render(request,'index.html',{'type':type,'msg':'Please Provide appropriate Details!'})

def HRsignin(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    type = 'hr_login'
    HRRegistration = HR_Registration.objects.filter(email=uname,password=upass)
    if  HRRegistration:
        return render(request,'hr.html',{'hr':HRRegistration,'email':uname})
    else:
        return render(request,'index.html',{'type':type,'msg':'wrong username or pass'})

def Applicantlogin(request):
    type = request.GET.get('type')
    return render(request, 'index.html', {'type': type})

def Applcantsignup(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    type = 'applicant_login'

    if password == repassword:
        ApplicantRegistration = Applicant_Registration(name=name, password=password, email=username, phone=phone)
        ApplicantRegistration.save()
        return render(request, 'index.html', {'type': type})
    else:
        return render(request, 'index.html', {'type': type, 'msg': 'Please Provide appropriate Details!'})

def Applcantsignin(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    type = 'applicant_login'
    ApplicantRegistration = Applicant_Registration.objects.filter(email=uname, password=upass)
    if ApplicantRegistration:
        return render(request, 'applicant.html', {'details': ApplicantRegistration})
    else:
        return render(request, 'index.html', {'type': type, 'msg': 'wrong username or pass'})

def Uploadresume(request):
    type = request.GET.get('type')
    print(type)
    # form upload resume code
    if request.method =='POST':
        resume = ApplicantResume(request.POST,request.FILES)
        if ApplicantResume.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('file Uploaded Successfully!')
        else:
            resume = ApplicantResume()
    return render(request,'applicant.html',{'type':type,'resume':resume})

def Managerloginpage(request):
    type = request.GET.get('type')
    return render(request, 'index.html', {'type': type})

def Managersignin(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    type = 'manager_login'
    ManagerRegister = Manager_Registration.objects.filter(email=uname,password=upass)
    if ManagerRegister:
        return render(request,'manager.html',{'details':ManagerRegister,'email':uname})
    else:
        return render(request,'index.html',{'type':type,'msg':'invalid username or password'})

def Interviewerloginpage(request):
    type = request.GET.get('type')
    return render(request, 'index.html', {'type': type})

def Interviewersignin(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('upass')
    type = 'interviewer_login'
    InterviewerRegistration = Interviewer_Registration.objects.filter(email=uname,password=upass)
    if InterviewerRegistration:
        return render(request,'interviewer.html',{'details':InterviewerRegistration,'email':uname})
    else:
        return render(request,'index.html',{'type':type,'msg':'invalid username or password'})

def RegisterManager(request):
    email = request.GET.get('email')
    print(email)
    ManagerRegistration = Manager_Registration.objects.all()
    print(ManagerRegistration)
    return render(request,'hr.html',{'email':email,'reg_manager':ManagerRegistration})

def Managersignup(request):
    type = "register_manager"
    return render(request,'hr.html',{'register_manager':type})

def ManagerRegister(request):
    name= request.POST.get('name')
    username= request.POST.get('username')
    password= request.POST.get('password')
    phone= request.POST.get('phone')
    email= request.POST.get('email') # getting data from hidden field
    reg_manager = "reg_manager"
    ManagerRegistration = Manager_Registration(name=name,email=username,password=password,phone=phone)
    ManagerRegistration.save()
    return render(request,'hr.html',{'reg_manager':reg_manager,'email':email})

def RegisterInterviewer(request):
    type = 'register_interviewer'
    return render(request,'manager.html',{'type':type})

def interviewerregister(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    type = "register_interviewer"
    InterviewerRegistration = Interviewer_Registration(name=name, email=username, password=password, phone=phone)
    InterviewerRegistration.save()
    return render(request, 'manager.html', {'type': type})


def UpdateResult(request):
    type = request.GET.get('type')
    print(type)
    return render(request,'interviewer.html',{'type':type})


def Viewmanager(request):
    email = request.GET.get('email')
    manager = Manager_Registration.objects.all()
    return render(request,'hr.html',{'email':email,'manager':manager})


def Managerupdate(request):
    email = request.POST.get('email')
    uname = request.POST.get('uname')
    print(email)
    print(uname)
    manager = Manager_Registration.objects.filter(email=uname)
    return render(request,'hr.html',{'email':email,'managerupdate':manager})


def managerupdated(request):
    name = request.POST.get('name')
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    manager = Manager_Registration(name=name,email=uname,phone=phone,password=password)
    manager.save()
    # details = Manager_Registration.objects.filter()
    return render(request,'hr.html',{'manager':manager,'email':email})


def managerdelete(request):
    email = request.POST.get('pk')
    Manager_Registration.objects.filter(email=email).delete()
    details = Manager_Registration.objects.all()
    return render(request,'hr.html',{'type':'view_manager','details':details})


def HRprofile(request):
    email = request.GET.get('email')
    HRRegistration = HR_Registration.objects.filter(email=email)
    print(HRRegistration)
    return render(request,'hr.html',{'email':email,'hr':HRRegistration})

def viewinterviewer(request):
    # type = request.POST.get('type')
    interviewer = Interviewer_Registration.objects.all()
    return render(request,'manager.html',{'type':'view_interviewer','details':interviewer})

def interviewerupdate(request):
    uname = request.POST.get('uname')
    interviewer = Interviewer_Registration.objects.filter(email=uname)
    return render(request,'manager.html',{'type':'interviewer_update','interviewerdetails':interviewer})

def interviewersave(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    uname = request.POST.get('uname')
    password = request.POST.get('password')
    interviewer = Interviewer_Registration(name=name, phone=phone, email=uname, password=password)
    interviewer.save()
    return render(request, 'manager.html', {'type':'interviewer_update','msg':' Data updated'})


def interviewerdelete(request):
    uname = request.POST.get('uname')
    interviewer = Interviewer_Registration.objects.filter(email=uname).delete()
    return render(request,'manager.html',{'type':'interviewer_update','msg':'Data Deleted'})