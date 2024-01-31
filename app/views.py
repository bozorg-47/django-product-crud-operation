from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.conf import settings
from django.http import FileResponse
import os
### for email ###
import smtplib

from email.message import EmailMessage


def product(request):
    if request.method=='POST':
        products=Product.objects.filter(name__contains=request.POST.get('search'))
    else:
        products=Product.objects.all()
    data={
      'products':products
    }
    return render(request,"product.html",data)

def createData(request):
    if request.method=='POST':
        names=request.POST.get('name')
        images=request.FILES['image']
        price=request.POST.get('price')
        add=Product(name=names,price=price,image=images)
        add.save()
    return redirect('/')

def deleteData(request):
    if request.method=='POST':
        id=request.POST.get('id')
        dele=Product.objects.get(pk=id)
        dele.delete()
        return redirect('/')


def updatedata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        images=request.FILES['image']
        price=request.POST.get('price')
        id=request.POST.get('id')
        upda=get_object_or_404(Product, pk=id)
        upda.name=name  
        upda.image=images  
        upda.price=price  
        upda.save()
    return redirect('/')





























# def Yourdef(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         description=request.POST.get('description')
#         images=request.FILES['image']
#         add=YourModel(name=name,description=description,image=images)
#         add.save()
#     stu=YourModel.objects.all()
#     data={
#       'stu':stu
#     }
#     return render(request,"index.html",data)
# def deletedata(request,id):
#     if request.method=='POST':
#         dele=YourModel.objects.get(pk=id)
#         dele.delete()
#         return redirect('/')
# def updatedata(request,id):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         description=request.POST.get('description')
#         images=request.FILES['image']
#         upda=get_object_or_404(YourModel, pk=id)
#         upda.name=name  
#         upda.description=description  
#         upda.image=images  
#         upda.save()
#         return redirect('/')
#     stu=YourModel.objects.get(pk=id)
#     data={'stu':stu}
#     return render(request,'updatestudent.html',data)