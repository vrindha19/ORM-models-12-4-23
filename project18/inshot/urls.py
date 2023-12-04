from django.urls import path
# from . import views
# from.views import create


# urlpatterns = [
#     path('members/', views.members, name='members'),
# ]

from .views import login

urlpatterns=[
    path ('login/',login,name='login'),
]

# urlpatterns=[
#     path('create/',create,name='create'),
# ]








