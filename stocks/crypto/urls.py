from django.urls import path
from crypto.views import index

urlpatterns = [
    path('', index, name="index"),
]
