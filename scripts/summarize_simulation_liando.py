import numpy as np
import pandas as pd
from scipy import stats
import sys
from numpy import random

#=== Get arguments
data=sys.argv[1]

# Distance,Hop,RTT,PLR
df=pd.read_csv(data, header=0, sep=",")

# Data for 400m
data_400m = df[df['Distance'] == "400m"]
for i in range(1,11):
    data_df=data_400m[data_400m['Hop'] == i]
    rtt_mean=np.mean(data_df['RTT'].to_numpy())
    rtt_dev=np.std(data_df['RTT'].to_numpy())
    rtt_sem=stats.sem(data_df['RTT'].to_numpy())
    plr_mean=np.mean(data_df['PLR'].to_numpy())
    plr_dev=np.std(data_df['PLR'].to_numpy())
    plr_sem=stats.sem(data_df['PLR'].to_numpy())

    print("400m,%s,%s,%s,%s,%s,%s,%s" % (i, rtt_mean, rtt_dev, rtt_sem, plr_mean, plr_dev, plr_sem))


# Data for 1km
data_1km = df[df['Distance'] == "1km"]
for i in range(1,11):
    data_df=data_1km[data_1km['Hop'] == i]
    rtt_mean=np.mean(data_df['RTT'].to_numpy())
    rtt_dev=np.std(data_df['RTT'].to_numpy())
    rtt_sem=stats.sem(data_df['RTT'].to_numpy())
    plr_mean=np.mean(data_df['PLR'].to_numpy())
    plr_dev=np.std(data_df['PLR'].to_numpy())
    plr_sem=stats.sem(data_df['PLR'].to_numpy())

    print("1km,%s,%s,%s,%s,%s,%s,%s" % (i, rtt_mean, rtt_dev, rtt_sem, plr_mean, plr_dev, plr_sem))



# Data for 5km
data_5km = df[df['Distance'] == "5km"]
for i in range(1,11):
    data_df=data_5km[data_5km['Hop'] == i]
    rtt_mean=np.mean(data_df['RTT'].to_numpy())
    rtt_dev=np.std(data_df['RTT'].to_numpy())
    rtt_sem=stats.sem(data_df['RTT'].to_numpy())
    plr_mean=np.mean(data_df['PLR'].to_numpy())
    plr_dev=np.std(data_df['PLR'].to_numpy())
    plr_sem=stats.sem(data_df['PLR'].to_numpy())

    print("5km,%s,%s,%s,%s,%s,%s,%s" % (i, rtt_mean, rtt_dev, rtt_sem, plr_mean, plr_dev, plr_sem))


    
