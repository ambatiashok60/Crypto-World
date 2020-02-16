import pandas as pd
import numpy as np
import datetime
import calendar

import os 

my_dir = os.path.join(os.path.dirname(os.getcwd()), 'stocks/static/data')
df = pd.read_csv(os.path.join(my_dir, 'BCH-USD.csv'))
print(df.head())
def dataframe():
    return df["Close"].values