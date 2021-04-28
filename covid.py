#import libraries and modules required
import pandas as pd
import matplotlib.pyplot as plt 
import datetime as dt
import numpy as np

#filtering through the csv file for Nepal and India's covid data 
# and keeping only some of it (date, location, total cases, 
# new cases, new cases smoothed, new deaths smoothed)

df = pd.read_csv('datasets/covid_data.csv', index_col=0 )
df.set_index('date', inplace=True)
df = df.iloc[:,[1,2,3,4,7]]
df_ind = df.copy()[df['location'] == 'India'].fillna(0)
df_nep = df.copy()[df['location'] == 'Nepal'].fillna(0)

#converting string dates to datetime objects for proper formatting later
df_nep['date'] = pd.to_datetime(list(df_nep.index)) 
nep_date = list(df_nep['date'])
nep_new_cases = np.array(df_nep['new_cases_smoothed'])
df_ind['date'] = pd.to_datetime(list(df_ind.index)) 
ind_date = list(df_ind['date'])
ind_new_cases = np.array(df_ind['new_cases_smoothed'])
