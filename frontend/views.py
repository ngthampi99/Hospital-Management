from django.shortcuts import render,redirect
from backend.models import Departmentdb,Doctordb
from frontend.models import Registerdb,Appointmentdb
# from django.contrib import messages


# Create your views here.

def home(request):
    dep = Departmentdb.objects.all()
    doc = Doctordb.objects.all()

    return render(request,"homepage.html",{'dep':dep,'doc':doc})

def aboutpage(request):
    doc = Doctordb.objects.all()
    return render(request,"aboutus.html",{'doc':doc})

def servicepage(request):
    return render(request,"services.html")

def departmentpage(request):

    dep = Departmentdb.objects.all()




    return render(request,"department.html",{'dep':dep})

def deptsingle(request,dept_id):

    dept = Departmentdb.objects.get(id=dept_id)

    return render(request,"singledept.html",{'dept':dept})

def doctorpage(request):
    doc = Doctordb.objects.all()
    return render(request,"doctor.html",{'doc':doc})

def docsingle(request,doc_id):

    doct = Doctordb.objects.get(id=doc_id)

    return render(request,"singledoc.html",{'doct':doct})

def regpage(request):
    return render(request,"reg.html")

def savereg(request):

    if request.method=="POST":
        una = request.POST.get("uname")
        ema = request.POST.get("email")
        pwd = request.POST.get("pass")
        mob = request.POST.get("mobile")

        obj = Registerdb(User_Name=una,Email_ID=ema,Password=pwd,Mob_No=mob)

        obj.save()

        return redirect(regpage)

def userlogin(request):

    if request.method=="POST":
        una = request.POST.get("uname")
        pwd = request.POST.get("pass")
        if Registerdb.objects.filter(User_Name=una,Password=pwd).exists():
            request.session["User_Name"]=una
            request.session["Password"]=pwd


            return redirect(home)
        else:
            return redirect(regpage)

    return redirect(regpage)

def userlogout(request):
    del request.session['User_Name']
    del request.session['Password']
    # messages.success(request, "Session Expired.Please Log In to Continue...!")
    return redirect(regpage)

def appointpage(request):
    doc = Doctordb.objects.all()
    return render(request,"appoint.html",{'doc':doc})

def saveappoint(request):
    if request.method=="POST":
        dept = request.POST.get('dep')
        doct = request.POST.get('doc')
        dob = request.POST.get('date')
        cna = request.POST.get('name')
        mob = request.POST.get('phone')
        msg = request.POST.get('message')


        obj = Appointmentdb(Department=dept,Doctor=doct, DOB=dob,Name=cna,Mobile=mob,Message=msg)
        obj.save()
        # messages.success(request, "Appointment Booked Sucessfully.We will Contact you Soon...")
        return redirect(confirmpage)

def confirmpage(request):
        return render(request,"conform.html")

def contactpage(request):
    return render(request,"contact.html")



