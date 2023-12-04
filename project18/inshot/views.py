from django.shortcuts import render
# from django.http import HttpResponse

# # def members(request):
# #     return HttpResponse("Hello world!")

# from .models import loginInfo

# def login (request):
#     if request.POST:
#         username=request.POST.get ('username')
#         password=request.POST.get ('password')
#         login_obj=loginInfo(username=username,password=password)
#         login_obj.save()
#         return render (request,"login.html")
    
from .models import loginInfo

def login (request):
    if request.POST:
        username=request.POST.get ('username')
        password=request.POST.get ('password')
        # desc=request.POST.get ('summary')
        Movie_obj=loginInfo(username=username,password=password)
        Movie_obj.save()
    return render (request,"login.html")


# from django.http import HttpResponse
# from django.template import loader

# def members(request):
#   template = loader.get_template('hello.html')
#   return HttpResponse(template.render())
