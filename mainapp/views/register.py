from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Errors are automatically passed with the form to the template
            pass
    
    return render(request, 'mainapp/register.html', {'form': form})

