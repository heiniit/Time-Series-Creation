import pandas as pd
import numpy as np

# Simple helper for representing somewhat reasonable hourly profile
def HourProfile(hour):
    if hour < 7:
        return 1.0
    if hour == 8:
        return 1.1
    if hour == 9:
        return 1.2
    if hour >= 10 and hour < 16:
        return 1.4
    if hour == 16:
        return 1.3
    else:
        return 1.1

# Series creation
rng = pd.date_range('1/1/2017', periods=24*365, freq='H')
ts = pd.Series(0.0, index=rng)

# Value calculation
for i in range(0, ts.shape[0]):
    if ts.index[i].dayofweek < 5: #not weekend
        ts[i] = 1.8*HourProfile(ts.index[i].hour) + np.random.rand()
    else: #weekend
        ts[i] = HourProfile(ts.index[i].hour) + np.random.rand() * 0.3

# Make a data frame and export that
df=pd.DataFrame(data=ts, columns = ["value"])
df.to_csv("C:\\temp\\TsData.csv")
