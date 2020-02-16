from django.shortcuts import render
from crypto.functions.bch_usd import dataframe

# Create your views here.


def index(request):
    func =  dataframe()
    return render(request,"crypto/crypto.html",{"func" : func})