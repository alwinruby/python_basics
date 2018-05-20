# quandl.ApiConfig.api_key = "YOURAPIKEY"


# Project Goal
# You want to track the daily percentage change of one of the three equities that you are interested in.
#
# Once, you've selected one equity to track, you want to notify yourself, when the price of that equity changes by a percentage that you specify.
#
# Note that the notification can be by email or sms.

#
# Sub goals to achieve
# Plot the adjusted closing price for one of the selected equity between the period 2017-01-01 and 2018-01-01.
# Plot the 50 day simple moving average for the selected equity over the same time period
# Plot the adjusted closing price of the three selected equities on the same graph between the period 2017-01-01 and 2018-01-01.
# Calculate the daily percentage change of the adjusted closing price for the three selected equities between the period 2017-01-01 and 2018-01-01.
# Plot a histogram of the daily percentage change, for each of the three equities and all on the same plot. You can use other plots to also identify the most volatile equity.
# Choose one of the equity to track daily and write a python script which achieves the following.
# Get the price data for the equity between the period of the current day - 1 and current day - 2.
# Calculate the absolute percentage change of the adjusted closing price.
# If the percentage is greater than or equal to threshold value which you set for yourself, then send a notification to your email or an sms to your phone.


import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)

from datetime import datetime
from datetime import timedelta
from local import API_KEY

quandl.ApiConfig.api_key = API_KEY
QUANDL_CODE = 'MSFT' #Quadl code of the equity you want to track - Microsoft
EMAIL = 'alwinsolanky@gmail.com' # Your email


if __name__ == '__main__':

    quandl_equity_code = QUANDL_CODE
    # data = quandl.get(quandl_equity_code, start_date='2018-03-23', end_date='2018-03-30')
    # data = quandl.get(quandl_equity_code, start_date='2017-01-01', end_date='2018-01-30')
    data = quandl.get('EOD/AAPL', start_date='2017-02-05', end_date='2017-09-12')
