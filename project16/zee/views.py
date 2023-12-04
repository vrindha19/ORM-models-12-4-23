from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.



# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")


    
from .models import RegisterInfo

def register(request):
    if request.POST:
        Name=request.POST.get ('Name')
        Username=request.POST.get ('Username')
        Email=request.POST.get ('Email')
        Password=request.POST.get ('Password')
        Confirmpassword=request.POST.get ('Confirmpassword')
        # desc=request.POST.get ('summary')
        register_obj=RegisterInfo(Name=Name,Username=Username,Email=Email,Password=Password,Confirmpassword=Confirmpassword)
        register_obj.save()
    return render (request,"register.html")


