from django.shortcuts import render
from .forms import ApplicationInput
# Create your views here.
def home(request):
    context ={"form":ApplicationInput()}
    if request.method == "POST":
        print(request.POST)
        form = ApplicationInput(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"practice1/home.html",context)