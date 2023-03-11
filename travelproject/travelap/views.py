from django.http import HttpResponse
from django.shortcuts import render
from .models import place, about


# Create your views here.
# def demo(request):
#     return render(request,"ind.html")
#
# def about(request):
#     return HttpResponse("hello")
# def new (request):
#      name="u doing "
#      return render(request,"new.html",{'jes':name})
# def new1(request):
#     return render(request,"new1.html")
# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"addd.html",{'result':res,'result2':sub,'result3':div,'result4':mul})
def ind(request):
    obj=place.objects.all()
    objj=about.objects.all()

    return render(request,"index.html",{'result':obj,'result2':objj})

