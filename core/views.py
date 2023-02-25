from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def content(request):
    return render(request, "core/content.html")


def system(request):
    return render(request, "core/system.html")
