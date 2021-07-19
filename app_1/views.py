
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app_1.forms import NewUser,Horrorform,Comicform,Historyform,Adventureform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from app_1.models import Adventure, Comic, History, Horror
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")



def register_req(request):
    if request.method == 'POST':
        print("hai")
        form = NewUser(request.POST) 
        if form.is_valid():
            print(form.cleaned_data["username"])
            user = form.save()
            login(request, user)
            messages.success(request,"registration successfull")
        else:
            messages.error(request,"registration unsuccessfull")
    form = NewUser()
    return render(request,"register.html", {"register_form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"login by {username} ")
                return HttpResponseRedirect(reverse('choice'))
            else:
                messages.error(request,"invalid username and password")
        else:
            messages.error(request,"invalid username and password")
    form = AuthenticationForm
    return render(request,"login.html",{"login_form":form})

def logout_req(request):
    logout(request)
    messages.info(request,"you have successfully logged out ")
    return redirect('home') 


def choice(request):
    return render(request,'choice.html')


def createhorror(request):
    if request.method=='POST':
        form = Horrorform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("Book")
            fs = FileSystemStorage()
            file = fs.save(upload_image.name,upload_image)
            user.book=file
            form.save()
            messages.success(request,"your product is created")
    form = Horrorform()
    return render(request,"createh.html",{'form':form})

def readhorror(request):
    var = Horror.objects.all()
    return render(request,"readh.html",{'form':var})

def modifyhorror(request,id):
    var = Horror.objects.get(id=id)
    if request.method=='POST':
        form=Horrorform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            form.save()
            messages.success(request,"your product is created in the db without image ")
    return render(request,"modifyh.html",{'form':var})

def deletehorror(request,id):
    var=Horror.objects.get(id=id)
    var.delete()
    var1=Horror.objects.all()
    return HttpResponseRedirect('/app_1/readh/')



def createcomic(request):
    if request.method=='POST':
        form = Comicform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("Book")
            fs = FileSystemStorage()
            file = fs.save(upload_image.name,upload_image)
            user.book=file
            form.save()
            messages.success(request,"your product is created")
    form = Comicform()
    return render(request,"createc.html",{'form':form})

def readcomic(request):
    var = Comic.objects.all()
    return render(request,"readc.html",{'form':var})

def modifycomic(request,id):
    var = Comic.objects.get(id=id)
    if request.method=='POST':
        form=Comicform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            form.save()
            messages.success(request,"your product is created in the db without image ")
    return render(request,"modifyc.html",{'form':var})

def deletecomic(request,id):
    var=Comic.objects.get(id=id)
    var.delete()
    var1=Comic.objects.all()
    return HttpResponseRedirect('/app_1/readc/')



def createhistory(request):
    if request.method=='POST':
        form = Historyform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("Book")
            fs = FileSystemStorage()
            file = fs.save(upload_image.name,upload_image)
            user.book=file
            form.save()
            messages.success(request,"your product is created")
    form = Historyform()
    return render(request,"createhis.html",{'form':form})

def readhistory(request):
    var = History.objects.all()
    return render(request,"readhis.html",{'form':var})

def modifyhistory(request,id):
    var = History.objects.get(id=id)
    if request.method=='POST':
        form=Historyform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            form.save()
            messages.success(request,"your product is created in the db without image ")
    return render(request,"modifyhis.html",{'form':var})

def deletehistory(request,id):
    var=History.objects.get(id=id)
    var.delete()
    var1=History.objects.all()
    return HttpResponseRedirect('/app_1/readhis/')



def createadventure(request):
    if request.method=='POST':
        form = Adventureform(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            upload_image=request.FILES.get("Book")
            fs = FileSystemStorage()
            file = fs.save(upload_image.name,upload_image)
            user.book=file
            form.save()
            messages.success(request,"your product is created")
    form = Adventureform()
    return render(request,"createad.html",{'form':form})

def readadventure(request):
    var = Adventure.objects.all()
    return render(request,"readad.html",{'form':var})

def modifyadventure(request,id):
    var = Adventure.objects.get(id=id)
    if request.method=='POST':
        form=Adventureform(request.POST,request.FILES,instance=var)
        if form.is_valid():
            form.save()
            messages.success(request,"your product is created in the db without image ")
    return render(request,"modifyad.html",{'form':var})

def deleteadventure(request,id):
    var=Adventure.objects.get(id=id)
    var.delete()
    var1=Adventure.objects.all()
    return HttpResponseRedirect('/app_1/readad/')
