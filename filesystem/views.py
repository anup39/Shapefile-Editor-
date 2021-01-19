from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

datas=[]
# Create your views here.
class Newform(forms.Form):
    title=forms.CharField()
   

def upload(request):
    if request.method== "POST":
        form=Newform(request.POST,request.FILES)
        if form.is_valid():
            title_1=form.cleaned_data["title"]
            datas.append(title_1)
            print(datas)
            return HttpResponseRedirect(reverse("list"))
           
        else:
            return render(request,"upload.html",{"form":form})
        
    return render (request,"upload.html",{"form":Newform()})



def lists(request):
    return render (request,"lists.html",{"datas":datas})

