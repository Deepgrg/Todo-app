from django.shortcuts import render

def indexPage(request):
    context= {}
    return render(request , "task/indexPage.html", context)