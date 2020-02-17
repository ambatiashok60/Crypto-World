import pandas as pd
import numpy as np
import datetime
import calendar

def day_gain_loss(day, df):
    day_df = df.groupby('Day Name').get_group(day)
    gain_days = day_df[day_df["Day Gain"] > 0].shape[0]
    loss_days = day_df[day_df["Day Gain"] <= 0].shape[0]
    return gain_days, loss_days

def daily_change(df):
    return ((df["Close"] - df["Open"])/df["Open"]).values

def MonthName(date):
    year,month,day = date.split("-")
    return calendar.month_name[int(month)]

def year(date):
    year,month,day = date.split("-")
    return int(year)

def convert_date_into_datetime_format(date):
    year,month,day = date.split("-")
    return datetime.datetime(int(year),int(month),int(day))

def convert_date_to_string_format(date):
    year = str(date.year)
    month = str(date.month)
    if(len(month) < 2):
        month = '0' + str(month)
    day = str(date.day)
    if(len(day) < 2):
        day = '0' + str(day)
    return "-".join([year,month,day])

def gain_loss(day, days, df):
    day_df = df.groupby('Day Name').get_group(day)
    current_dates = day_df.apply(lambda x: convert_date_into_datetime_format(x["Date"]) + datetime.timedelta(days),axis = 1)
    upcoming_dates = current_dates.apply(lambda x: convert_date_to_string_format(x))
    closing_price = np.hstack([df[df["Date"] == item]["Close"].values for item in upcoming_dates])
    opening_price = day_df["Open"].values
    if(opening_price.shape == closing_price.shape):
        return (closing_price - opening_price)/opening_price
    else:
        return (closing_price - opening_price[:closing_price.shape[0]])/(opening_price[:closing_price.shape[0]])



