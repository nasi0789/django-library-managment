from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from datetime import datetime,timedelta,date
from django.contrib import messages


from django.http import HttpResponseRedirect


# Create your views here.

class HomeView(View):
    def get(self,request):
        # if request.user.is_authenticated:
        #     # return HttpResponseRedirect('afterlogin')
        return render(request,'index.html')

#for showing signup/login button for teacher
class AdminClickView(View):
    def get(self,request,*args, **kwargs):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect('afterlogin')
        return render(request,'adminclick.html')
    
class StudentClickView(View):
    def get(self,request,*args, **kwargs):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect('afterlogin')
        return render(request,'studentclick.html')
    
class AdminSignupView(View):
    def get(self,request):
        form=AdminSigupForm()
        return render(request,'adminsignup.html',{"form":form})
    def post(self,request):
            form=AdminSigupForm(data=request.POST)
            if form.is_valid():
                user=form.cleaned_data.get("username")
                pswd=form.cleaned_data.get("password1")
                fname=form.cleaned_data.get("first_name")
                lname=form.cleaned_data.get("last_name")
                User.objects.create_superuser(username=user,password=pswd,first_name=fname,last_name=lname)
                # user.set_password(user.password)
                # user.save()

        #         my_admin_group = Group.objects.get_or_create(name='ADMIN')
        #         my_admin_group[0].user_set.add(user)
                return redirect('admlog')
            return render(request,'adminsignup.html',{'form':form})
# class AdminSignupView(CreateView):
#     template_name="adminsignup.html"
#     form_class=AdminSigupForm
#     success_url=reverse_lazy("admlog")


class StudentSignupView(CreateView):
    def get(self,request):
        form1=StudentUserForm()
        form2=StudentExtraForm()

        return render(request,'studentsignup.html',{"form1":form1,"form2":form2})
    
    def post(self,request):
        form1=StudentUserForm()
        form2=StudentExtraForm()
        mydict={'form1':form1,'form2':form2}
        form1=StudentUserForm(request.POST)
        
        if form1.is_valid():
            enrlt=request.POST.get("enrollment")
            brch=request.POST.get("branch")
                # user.set_password(user.password)
            user=form1.save()
            StudentExtra.objects.create(enrollment=enrlt,branch=brch,user=user)

            # user.set_password(user.password)
            # user.save()
            # f2=form2.save(commit=False)
            # f2.user=user
            # user2=f2.save()
            print("252522222222222222222222222222222")
            # my_student_group = Group.objects.get_or_create(name='STUDENT')
            # my_student_group[0].user_set.add(user)
            return redirect("stdlog")
        # return render(request,'studentsignup.html',{"form1":form1})
        return render(request,'studentsignup.html',context=mydict)

class AdminLogView(FormView):
    template_name="adminlogin.html"
    form_class=AdminLogForm
    def post(self,request):
        form_data=AdminLogForm(data=request.POST)
        if form_data.is_valid():
            print("111111111111111111111111111111111")
            user=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user_ob=authenticate(request,username=user,password=pswd)
            print(user_ob)
            if user_ob.is_superuser==1:
                print("2222222222222222222222")
                login(request,user_ob)
                # messages.success(request,"Login Successful!!")
                return redirect("admhome")
        else:
            print("333333333333 3")

            # messages.error(request,"Login Failed!! Invalid Username or password!")
            return render(request,"adminlogin.html",{"form":form_data})  
class StudentLogView(FormView):
    template_name="studentlogin.html"
    form_class=StdLogForm
    def post(self,request):
        form_data=StdLogForm(data=request.POST)
        print(form_data,'lkoplo')
        if form_data.is_valid():
            user=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user_ob=authenticate(request,username=user,password=pswd)
            print(user_ob)
            print(user)
            print(pswd)
            if user_ob.is_superuser!=1:
                print(user_ob)
                login(request,user_ob)
                # messages.success(request,"Login Successful!!")
                return redirect("stdhome")
        else:
            # messages.error(request,"Login Failed!! Invalid Username or password!")
            return render(request,"log.html",{"form":form_data})  

 
class LgOut(View):
    def get(self,request):
        logout(request)
        return redirect("home")

class AdmHomeView(View):
    def get(self,request):
        return render(request,"adminafterlogin.html")
class StdHomeView(View):
    def get(self,request):
        return render(request,"studentafterlogin.html")

    
    
class AddBook(View):
    def get(self,request):
        form=BookForm()
        #now it is empty book form for sending to html
        return render(request,'addbook.html',{'form':form})
        
    def post(self,request):
        form=BookForm()
        #now this form have data from html
        form=BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bookadded.html')
        return render(request,'addbook.html',{'form':form})

class ViewBook(View):
    def get(self,request):
        books=Book.objects.all()
        return render(request,'viewbook.html',{'books':books})
    
def deletebookitem(request,id):
    cart=Book.objects.get(id=id)
    cart.delete()
    messages.error(request,"Book removed")
    return redirect("viewbk")

class IssueBook(View):
    def get(self,request):
        form=IssuedBookForm()
        return render(request,'issuebook.html',{'form':form})

    def post(self,request):
        form=IssuedBookForm()
        #now this form have data from html
        form=IssuedBookForm(request.POST)
        if form.is_valid():
            obj=IssuedBook()
            obj.enrollment=request.POST.get('enrollment2')
            obj.isbn=request.POST.get('isbn2')
            obj.save()
            return render(request,'bookissued.html')
        return render(request,'issuebook.html',{'form':form})
 
class ViewIssueBook(View):
    def get(self,request):
        issuedbooks=IssuedBook.objects.all()
        li=[]
        print(li)
        for ib in issuedbooks:
            issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
            expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
            #fine calculation
            days=(date.today()-ib.issuedate)
            print(date.today())
            d=days.days
            print(d)
            fine=0
            if d>15:
                day=d-15
                fine=day*10


            books=list(Book.objects.filter(isbn=ib.isbn))
            print
            print(books)
            students=list(StudentExtra.objects.filter(enrollment=ib.enrollment))
            print(students)
            i=0
            for l in books:
                t=(students[i].get_name,students[i].enrollment,books[i].name,books[i].author,issdate,expdate,fine)
                i=i+1
                li.append(t)
        return render(request,'viewissuedbook.html',{'li':li})
class ViewStudent(View):
       
    def get(self,request):
        students=StudentExtra.objects.all()
        return render(request,'viewstudent.html',{'students':students})

class ViewIssueBookByStudent(View):  
    def get(self,request):
        print('lllllllklkl')
        student=StudentExtra.objects.filter(user_id=request.user.id)
        issuedbook=IssuedBook.objects.filter(enrollment=student[0].enrollment)

        li1=[]

        li2=[]
        for ib in issuedbook:
            books=Book.objects.filter(isbn=ib.isbn)
            for book in books:
                t=(request.user,student[0].enrollment,student[0].branch,book.name,book.author)
                li1.append(t)
            issdate=str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
            expdate=str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)
            #fine calculation
            days=(date.today()-ib.issuedate)
            print(date.today())
            print(days,'oooo')
            d=days.days
            print(d)
            fine=0
            if d>0:
                day=d-0
                fine=day*10
            t=(issdate,expdate,fine)
            li2.append(t)

        return render(request,'viewissuedbookbystudent.html',{'li1':li1,'li2':li2})
