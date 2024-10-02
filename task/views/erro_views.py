from django.shortcuts import render


def erro(request):
    return render(request,'tasks/erro.html')