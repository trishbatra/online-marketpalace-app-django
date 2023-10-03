from django.shortcuts import redirect, render
from items.models import category,items
from .forms import signUpForm
# Create your views here.
def index(request):
    itemss = items.objects.all()
    cat = category.objects.all()
    return render(request, 'core/index.html', {
        'c' : cat,
        'i' : itemss
    })
def contact(request):
    return render(request, 'core/contact.html')

def signUP(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        
        form = signUpForm()

    return render(request, 'core/signup.html', {
        "f" : form
    })

