from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import LoginForm,SignupForm,UpdateForm,ImageForm
from django.contrib.auth import logout as logouts
from django.contrib import messages
from . models import Images,ImagesT
from . models import submit
from project9 import settings
from django.core.mail import send_mail

def hello(request):
    return HttpResponse('hello')
def index(request):
    name='thulasi'
    return render(request,'index.html',{'data':name})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=submit.objects.get(Email=email)
            if not user:
                messages.warning(request,'email donot exist')
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,'password incorrect')
                return redirect('/login')
            else:
                messages.success(request,"login success")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            photo=form.cleaned_data['Photo']

            user=submit.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exist')
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,'passwordmismatch')
                return redirect('/signup')
            else:
                tab=submit(Name=name,Age=age,Place=place,Email=email,Password=password,Photo=photo)
                tab.save()
                messages.success(request,"data saved")
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

def home(request,id):
    users=submit.objects.get(id=id)
    return render(request,'home.html',{'users':users})


def update(request,id):
    users=submit.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=users)
        if form.is_valid():
                form.save()
                messages.success(request,"UPDATE SUCCESSFULLY")
                return redirect('/home/%s'% users.id)
    else:
        form=UpdateForm(instance=users)
    return render(request,'update.html',{'form':form,'users':users})

def logout(request):
    logouts(request)
    messages.success(request,'logout successfully')
    return redirect('/')

def showimages(request):
    users=ImagesT.objects.all()
    return render(request,'gallery.html',{'users':users})

def details(request,id):
    users=ImagesT.objects.get(id=id)
    return render(request,'details.html',{'users':users})

def mail(request):
    if request.method=="POST":
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email')
        cmessage=request.POST.get('contact_message')
        toemail="thulasis478@gmail.com"
        res=send_mail(cname,cmessage,settings.EMAIL_HOST_USER,[toemail],fail_silently=False)
        if(res == 1):
            msg="MAIL SENT SUCCESSFULLY"
        else:
            msg="MAIL COULD NOT SEND"
        return HttpResponse(msg)
    else:
        return render(request,'index.html')

# Create your views here.
