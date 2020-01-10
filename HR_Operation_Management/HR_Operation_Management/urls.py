"""HR_Operation_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from HR import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('home/', views.showhome),

    path('hrloginpage/', views.Hrlogin),
    path('hrprofile/',views.HRprofile),
    path('hrsignup/', views.HRsignup),
    path('hrsignin/', views.HRsignin),
    path('registermanager/', views.RegisterManager),
    path('managersignup/', views.Managersignup),
    path('managerregister/', views.ManagerRegister),
    path('viewmanager/', views.Viewmanager),
    path('managerupdate/', views.Managerupdate),
    path('managerupdated/', views.managerupdated),
    path('managerdelete/', views.managerdelete),



    path('applicantloginpage/', views.Applicantlogin),
    path('applcantsignup/', views.Applcantsignup),
    path('applicantsignin/', views.Applcantsignin),
    path('uploadresume/', views.Uploadresume),


    path('managerloginpage/', views.Managerloginpage),
    path('managersignin/', views.Managersignin),
    path('registerinterviewer/', views.RegisterInterviewer),
    path('interviewerregister/', views.interviewerregister),
    path('viewinterviewer/', views.viewinterviewer),
    path('interviewerupdate/', views.interviewerupdate),
    path('interviewersave/', views.interviewersave),
    path('interviewerdelete/', views.interviewerdelete),

    path('interviewerloginpage/', views.Interviewerloginpage),
    path('interviewersignin/', views.Interviewersignin),
    path('updateresult/', views.UpdateResult),







]
