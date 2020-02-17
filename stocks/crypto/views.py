from django.shortcuts import render
from crypto.staticfiles.functionfiles.bch_usd import daily_change
import pandas as pd
import os

# Create your views here.

my_dir = os.path.join(os.getcwd(),"crypto/staticfiles/datafiles")
file_path = os.path.join(my_dir,'BCH-USD.csv')
df = pd.read_csv(file_path)
print(df.head())
def index(request):
    change = daily_change(df)
    context = df.iloc[:,1:5].values
    zipped = zip(context,change)
    return render(request,"crypto/crypto.html",{"context" : context, "change" : change, "zipped" : zipped})
