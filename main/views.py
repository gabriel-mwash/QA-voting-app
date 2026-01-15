from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import userForm
from .models import user_data

# Create your views here.


def home(request):
    return HttpResponse("this is the home page, welcome")


def greeting(request):
    return HttpResponse("hello world")


def data(request):
    data = user_data.objects.all()
    return render(request, "data.html",
                  {"data": data})

def form_view(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")

    else:
        form = userForm()
    return render(request, "form.html",
                  {"form": form})


def success_view(request):
    return render(request, "success.html")
