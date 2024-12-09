#views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def user_dashboard(request):
    return render(request, 'user_dashboard.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()

            # Log the user in after registration
            login(request, user)

            # Redirect to a success page or home page
            return redirect('home')  # Update this with the actual name of the page you want to redirect to
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
