from django.urls import path
# from . import views



# urlpatterns = [
#     path('create/', views.create, name='create'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]



from .views import register

urlpatterns=[
    path ('register/',register,name='register'),
]

