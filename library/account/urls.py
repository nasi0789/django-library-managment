from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('adminclick',AdminClickView.as_view(),name="admclick"),
    path('studentclick',StudentClickView.as_view(),name="stdclick"),
    
    path('adminsignup',AdminSignupView.as_view(),name="admsigup"),
    path('studentsignup',StudentSignupView.as_view(),name="stdsigup"),
    
    # path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('adminlogin',AdminLogView.as_view(),name="admlog"),
    path('studentlogin',StudentLogView.as_view(),name="stdlog"),
    
    path('lgout',LgOut.as_view(),name="logout"),

    
    path('admaftrlog',AdmHomeView.as_view(),name="admhome"),
    path('stdaftrlog',StdHomeView.as_view(),name="stdhome"),
    
    path('addbook',AddBook.as_view(),name="addbk"),
    path('viewbook',ViewBook.as_view(),name="viewbk"),
    path("delcart/<int:id>",deletebookitem,name="delcart"),

    path('issuebook',IssueBook.as_view(),name="issuebk"),
    path('viewissuebook',ViewIssueBook.as_view(),name="vwissuebk"),
    path('viewstudent',ViewStudent.as_view(),name="viewstd"),
    path('viewissuedbookbystudent',ViewIssueBookByStudent.as_view(),name="viewbkbystd"),




]
