from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "pages/index.html")


def company(request):
    return render(request, "pages/company.html")


def about(request):
    return render(request, "pages/about.html")


def industries(request):
    return render(request, "pages/industries.html")


def technology(request):
    return render(request, "pages/technology.html")


def contact(request):
    return render(request, "pages/contact.html")

    