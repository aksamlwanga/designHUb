from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import TenantForm
from .models import Tenant,Temperature
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

# search method
def search(request):
    search_term = request.GET.get('search')
    data=Temperature.objects.filter(Q(userTempId__name__icontains=search_term)|Q(userTempId__company__icontains=search_term)|Q(userTempId__telephone__icontains=search_term)
    |Q(temperature__icontains=search_term)|Q(date_posted__icontains=search_term))
    return data
# edit value method
def edits(request):
    id = request.POST.get('submit') 
    data=Temperature.objects.filter(userTempId_id=id)
    return data

@login_required
def home(request):
     data= Temperature.objects.order_by('-date_posted')

     ids=[]
     newUniqueData=[]
    #  getting unique data
     for x in data:
      # check if exists in unique_list or not
      if x.userTempId.id not in ids:
          ids.append(x.userTempId.id)
          newUniqueData.append(x)
      data=newUniqueData
    #   search input
     if 'search' in  request.GET:
         data=search(request)
         
    # edit searched value
     if 'submit' in  request.POST:
         print( request.POST.get('submit'))
         data=edits(request)
         return render(request,'update.html',{'data':data})
    # add new value for the temperature
     if 'add' in  request.POST:
         id = request.POST.get('add') 
         temp=request.POST.get('temp')
         tempdata= Temperature(temperature=temp, userTempId=Tenant.objects.get(id=id))
         tempdata.save()
         data=Temperature.objects.filter(userTempId=Tenant.objects.get(id=id)).order_by('-date_posted')
         return render(request,'update.html',{'data':data})
        

         
     return render(request,'home.html',{'data':data})

@login_required
def register(request):
    # to check if the id of the searched element was submitted
    if 'submit' in  request.POST:
    
         data=edits(request)
         return render(request,'update.html',{'data':data}) 

    # to check for the search input
    if 'search' in  request.GET:
        data=search(request)
        return render(request,'home.html',{'data':data})   

    user=request.user
    # get data from the form or create one
    form=TenantForm(request.POST or None)
    if form.is_valid():
        try:
        #    getting the phone number just incase someone try to submit the same data
           tenantdata=Tenant.objects.get(telephone=form.cleaned_data.get('telephone'))
          
           tempdata = Temperature(temperature=form.cleaned_data.get('temperature'), userTempId=tenantdata)
           tempdata.save()
           messages.success(request, 'Update was successfully')
        except ObjectDoesNotExist:
        #    if no id found
           tenantdata = form.save(commit=False)
           tenantdata.user_id=user
           tenantdata.save()
           obj = Tenant.objects.get(id=tenantdata.id)
           tempdata = Temperature(temperature=form.cleaned_data.get('temperature'), userTempId=obj)
           tempdata.save()
           
           
           messages.success(request, 'New record was added succefully')
        finally:
           
           form=TenantForm(None)
           return render(request,'register.html',{'form':form})
        
        

    return render(request,'register.html',{'form':form})


