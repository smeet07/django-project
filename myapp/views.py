from django.shortcuts import render,redirect
from django.http import HttpResponse
import csv
from .models import  *
from .forms import MedCreateForm,MedSearchForm,MedUpdateForm,CreateUserForm,SellForm,PurchaseForm,reorder,CreateBillForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home1(request):
    return render(request,'myApp/initialhomepage.html')
def reports(request):
    return render(request,'myApp/reports.html')
def home(request):

    return render(request,'myapp/homepage.html')
def contact(request):
    return HttpResponse('contact')
def templateTagsDemo(request):
    name="smeet"
    list={'sample': name, 'Country': {'india','brazil'},'States':{'maharatshtra','rio'}}
    return render(request,'myapp/templatetagDemo.html',list)
def search(request):
    return render(request,'myapp/search.html')
def Add(request):
    return render(request,'myapp/Add.html')

def list_items(request):
    title="list of list_items"
    header="MEDICINES"
    form= MedSearchForm(request.POST or None)
    queryset=Medicine.objects.all()
    context = {
        "title":title,
        "queryset":queryset,
        "header":header,
        "form":form,
    }
    if request.method=='POST':
        queryset=Medicine.objects.filter(company__icontains=form['company'].value(),name__icontains=form['name'].value())
        if form['export_to_csv'].value()==True:
            response=HttpResponse(content_type='text/csv')
            response['Content-Disposition']='attachment;filename="list  of medicine.csv"'
            writer=csv.writer(response)
            writer.writerow(['name','company','quantity'])
            instance=queryset
            for medicine in instance:
                writer.writerow([medicine.name,medicine.company,medicine.quantity])
                return response
        context={
            "form":form,
            "header":header,
            "queryset":queryset,

        }

    return render(request,'myApp/list_items.html',context)
def add_items(request):
    form = MedCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        "title": "Add medicine",

    }
    return render(request,'myApp/add_items.html',context)
def add_items1(request):
    form = MedCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Saved Successfully')
        return redirect('/list_items')

    context = {
        'form': form,
        "title": "Add medicine",

    }
    return render(request,'myApp/Add.html',context)
def update_items(request,pk):
    queryset=Medicine.objects.get(id=pk)
    form=MedUpdateForm(instance=queryset)
    if request.method=='POST':
        form=MedUpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Updated')
            return redirect('/list_items')
    context={
        "form":form,
    }
    return render(request,'myApp/Add.html',context)
def loginPage(request):

    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home1')
       else :
           messages.info(request,'Username or password incorrect')
    context={}
    return render(request,'myApp/login.html',context)
def registerPage(request):
    form=CreateUserForm
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created')
            return redirect('login')

    context={
        "form":form,
    }
    return render(request,'myApp/register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def delete_items(request,pk):
    queryset=Medicine.objects.get(id=pk)
    if request.method=='POST':
        queryset.delete()
        messages.success(request, 'Data Deleted')
        return redirect('delete')

    return render(request,'myApp/delete_items.html')
def delete(request):
    title = "Delete items"

    queryset = Medicine.objects.all()
    context = {
        "title": title,
        "queryset": queryset,

    }
    return render(request,'myApp/delete.html',context)
def details(request,pk):


    queryset = Medicine.objects.get(id=pk)
    context = {
        "title": queryset.name,
        "queryset": queryset,

    }
    return render(request,'myApp/details.html',context)
def sell_items(request,pk):
    queryset=Medicine.objects.get(id=pk)
    form=SellForm(request.POST or None,instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity=instance.quantity-instance.sell_quantity
        messages.success(request,"sold successfully "+str(instance.quantity)+" of "+str(instance.name)+" left")
        instance.save()
        return redirect('/details/'+str(instance.id))
    context={
        "title":"sell"+str(queryset.name),
    "queryset":queryset,
        "form":form,

    }
    return render(request,'myApp/Add.html',context)
def purchase_items(request,pk):
    queryset=Medicine.objects.get(id=pk)
    form=PurchaseForm(request.POST or None,instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.quantity=instance.quantity+instance.purchase_quantity
        messages.success(request,str(instance.quantity)+" of "+str(instance.name)+" received")
        instance.save()
        return redirect('/details/'+str(instance.id))
    context={
        "title":"purchase"+str(queryset.name),
    "queryset":queryset,
        "form":form,

    }
    return render(request,'myApp/Add.html',context)
def reorder_level(request,pk):
    queryset=Medicine.objects.get(id=pk)
    form=reorder(request.POST or None,instance=queryset)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,'reorder level for '+str(instance.name)+' is updated')
        return redirect('/list_items')
    context={
        "queryset":queryset,
        "form":form,


    }
    return render(request,'myApp/Add.html',context)
def createbill(request):
        form = CreateBillForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Saved Successfully')
            return redirect('/list_items')

        context = {
            'form': form,
            "title": "Create Bill",

        }
        return render(request, 'myApp/Add.html', context)


