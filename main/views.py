from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import userForm, anotherForm, QnAForm
from .models import user_data, User

# Create your views here.


def home(request):
    if request.method == "POST":
        form = QnAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = QnAForm()
    return render(request, "index2.html", {"form": form})



def greeting(request):
    return HttpResponse("hello world")


def data(request):
    data = user_data.objects.all()
    return render(request, "data.html",
                  {"data": data})


# saving using model form ... highly recommended
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


# seprate the form from the model
# in the sense that we extract data from the form, and save it to db
def register_view(request):
    if request.method == "POST":
        form = anotherForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = User(username=username, email=email);
            user.save()

            return redirect("success")
    else:
        form = anotherForm()

    return render(request, "form2.html",
                  {"form": form})
