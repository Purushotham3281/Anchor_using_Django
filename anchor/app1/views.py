from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def fun1(request):
    
    return render(request,"home.html")
def fun2(request):
    
    return render(request,"contact.html")
def fun3(request):
    
    return render(request,"about.html")
def fun4(request):
    
    return render(request,"help.html")
def fun5(request,string):
    result=(string == string[::-1])
    context={"string":string,"result":result}
    return render(request,"polindrome.html",context)
    

