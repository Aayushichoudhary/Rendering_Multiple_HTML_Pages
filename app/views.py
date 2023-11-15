from django.shortcuts import render

# Create your views here.
def fun1(request):
    return render(request,'temp1.html')

def fun2(request):
    return render(request,'temp2.html')

def fun3(request):
    return render(request,'temp3.html')

def fun4(request):
    return render(request,'temp4.html')