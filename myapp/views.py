from django.shortcuts import render
import requests
# Create your views here.
def indexpage(request):
    return render(request,"index1.html")

def sportspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    response = url.json()
    sportsnews = response["data"]

    context = {
        "sportsnews": sportsnews,
    }
    return render(request,"sports.html",context)

def politicspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    response = url.json()
    politicsnews = response["data"]

    context = {
        "politicsnews": politicsnews,
    }
    return render(request,"politics.html",context)

def techpage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=technology")
    response = url.json()
    technews = response["data"]

    context = {
        "technews": technews,
    }
    return render(request,"technology.html",context)

def startuppage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=startup")
    response = url.json()
    startupnews = response["data"]

    context = {
        "startupnews": startupnews,
    }
    return render(request,"startup.html",context)

def businesspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=business")
    response = url.json()
    businessnews = response["data"]

    context = {
        "businessnews": businessnews,
    }
    return render(request,"business.html",context)

def sciencepage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=science")
    response = url.json()
    sciencenews = response["data"]

    context = {
        "sciencenews": sciencenews,
    }
    return render(request,"science.html",context)