from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'base_generic.html')
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')


    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html',{'form': form})



from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')



def logout_view(request):
    logout(request)
    # Redirect to home page or any other page after logout
    return redirect(reverse_lazy('home'))