from django.shortcuts import redirect, render
from .forms import QnAForm


def home(request):
    if request.method == "POST":
        form = QnAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = QnAForm()
    return render(request, "index2.html",
                  {"form": form})


def success_view(request):
    return render(request, "success.html")
