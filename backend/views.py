from django.shortcuts import render,redirect
from backend.models import Departmentdb,Doctordb
from frontend.models import Appointmentdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def indexpage(request):
    return render(request,"index.html")



def Dept(request):
    return render(request,"adddept.html")

def savedept(request):

    if request.method=="POST":
        dna =request.POST.get('dname')
        des =request.POST.get('descr')
        img =request.FILES['image']

        obj = Departmentdb(Dept_Name=dna,Description=des,Image=img)
        obj.save()
        messages.success(request, "Department Saved Sucessfully...!")
        return redirect(Dept)

def Deptdisplay(request):
    data = Departmentdb.objects.all()

    return render(request,"displaydept.html",{'data':data})

def editdept(request,dataid):
    data = Departmentdb.objects.get(id=dataid)

    return render(request,"editdepartment.html",{'data':data})

def updatedept(request,dataid):

    if request.method=="POST":
        dna = request.POST.get("dname")
        des = request.POST.get("descr")
        try :
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:

            file = Departmentdb.objects.get(id=dataid).Image

        Departmentdb.objects.filter(id=dataid).update(Dept_Name = dna, Description = des,Image=file)
        messages.success(request,"Updated Sucessfully...!")
        return redirect(Deptdisplay)


def deletedept(request,dataid):
    data = Departmentdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted Sucessfully...!")
    return redirect(Deptdisplay)

# end department section.....

# Doctors section

def adddoc(request):
    dep = Departmentdb.objects.all()
    return render(request,"adddoctor.html",{'dep':dep})

def savedoc(request):
    if request.method=="POST":
        dna = request.POST.get('dname')
        don = request.POST.get('name')
        des = request.POST.get('descr')
        qua = request.POST.get('qualif')
        fof = request.POST.get('expert')
        img = request.FILES['dimage']

        obj = Doctordb(Dept_Name=dna,Doctor_Name=don, Description=des,Qualification=qua,Expertise_Field=fof,Doc_Image=img)
        obj.save()
        messages.success(request, "Doctor Details Saved Sucessfully...!")
        return redirect(adddoc)

def displaydoc(request):
    data = Doctordb.objects.all()
    return render(request,"displaydoctor.html",{'data':data})

def editdoc(request,docid):
    dep = Departmentdb.objects.all()
    doc = Doctordb.objects.get(id=docid)
    return render(request,"editdoctor.html",{'dep':dep,'doc':doc})

def updatedoc(request,docid):
    if request.method=="POST":
        dna = request.POST.get("dname")
        don = request.POST.get("name")
        des = request.POST.get("descr")
        qua = request.POST.get("qualif")
        fof = request.POST.get("expert")
        try :
            img = request.FILES["dimage"]
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:

            file = Doctordb.objects.get(id=docid).Doc_Image

        Doctordb.objects.filter(id=docid).update(Dept_Name =dna,Doctor_Name=don, Description = des,Qualification = qua,Expertise_Field=fof,Doc_Image=file)
        messages.success(request,"Updated Sucessfully...!")
        return redirect(displaydoc)

def deldoc(request,docid):

    doc = Doctordb.objects.filter(id=docid)
    doc.delete()
    messages.success(request, "Deleted Sucessfully...!")
    return redirect(displaydoc)

def loginpage(request):
    return render(request,"addlogin.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():

            user = authenticate(username=uname,password=pwd)

            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request,"Login Sucessfully...")
                return redirect(indexpage)

            else:
                messages.success(request,"Invalid Response....")
                return redirect(admin_login)
        else:
            messages.success(request,"Invalid Response....")
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Session Expired.Please Log In to Continue...!")
    return redirect(loginpage)

def bookingpage(request):
    data = Appointmentdb.objects.all()

    return render(request,"displaypatient.html",{'data':data})





















