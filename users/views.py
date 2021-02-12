from django.shortcuts import render
from .forms import UserAuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login(request):
#    check if user is authenticated already
   if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    # login process
   if request.method=="POST":
        form=UserAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('home')
            else:
                print('User not found')
            
   else:
        
        form=UserAuthenticationForm()
    # If there were errors, we render the form with these
    # errors
   return render(request,'users.login.html',{'form':form})

# logout method
def logout(request):
    logout(request)