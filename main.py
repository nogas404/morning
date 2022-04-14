# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Downloading latest data

import requests


new_cases = requests.get('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv')

with open('new_cases.csv', 'wb') as f:
    f.write(new_cases.content)

# %%
# VARS

period_of_time = 30
country = 'Poland'

# %%
# opening file
data = pd.read_csv('new_cases.csv')

# extracting data from poland
data = data[[country]]

# last X days
y = data.tail(period_of_time)


# %%
# creating array with X days
x = np.arange(0, period_of_time, 1).reshape(period_of_time, 1)

# making DataFrame from array
x = pd.DataFrame(x)


# %%
# plotting

plt.ylabel(f'Cases in {country}')
plt.xlabel('Days')

plt.scatter(x, y)
    
plt.plot()
plt.savefig('img.jpg')

