from django.shortcuts import render
from django.http import HttpResponse
from .models import MyTable

# Create your views here.

def displaymessage(request):
    return HttpResponse('hellodjango')

def home(request):
    return HttpResponse('welcome home')

def personal(request,name):
    return HttpResponse(f'Hello {name}')


# def homepage(request):
#     return render(request,'homepage.html'
def homepage(request):
    msg="hi all welcome to my website."
    name='iam vishnu'
    return render(request,'homepage.html',{'m':msg,'n':name})  

def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def header(request):
    return render(request,'header.html')
def display(request,fname,lname):
    return render(request,'display.html',{'fname':fname,'lname':lname})

#database connection

#data insertion
def insert(request,nam,val):
    newrecord=MyTable()
    newrecord.name=nam
    newrecord.age=val
    newrecord.save()
    return HttpResponse("saved successfully")
#fetching datas
def display(request): 
    records = MyTable.objects.all()
    print(records.values())
    return HttpResponse(records.values())
#display in a html page
def displayform(request):
    records=MyTable.objects.all()
    return render(request,'displayform.html',{"r":records})
#display by name
def displaybyname(request,nam):
    records=MyTable.objects.filter(name=nam)
    return render(request,"displayform.html",{"r":records})

def displaybyage(request,age):
    records=MyTable.objects.filter(age__gte=age)
    return render(request,"displayform.html",{"r":records})

def updatebyid(request,cid,ageval):
    rec=MyTable.objects.get(id=cid)
    rec.age=ageval
    rec.save()
    records=MyTable.objects.all()
    return render(request,"displayform.html",{"r":records})

def deletebyname(request,nam):
    records=MyTable.objects.filter(name=nam)
    if records.exists():
        records.delete()
        msg="deleted successfully"
    else:
        msg="name does not exists"
    records=MyTable.objects.all()
    return render(request,"displayform.html",{"r":records,"msg":msg})

def deletebyid(request,cid):
    records=MyTable.objects.filter(id=cid)
    if records.exists():
        records.delete()
        msg="deleted successfully"
    else:
        msg="name does not exists"
    records=MyTable.objects.all()
    return render(request,"displayform.html",{"r":records,"msg":msg})


def deleteall(request):
    records=MyTable.objects.all()
    records.delete()
    records=MyTable.objects.all()
    msg='deleted all records'
    return render(request,"displayform.html",{"r":records,"msg":msg})