import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read stock data and parse into date and close
df = pd.read_csv('tesla.csv')
dates = df['Date']
close = df['Close']
x = np.arange(1,len(close)+1)

# polynomial fitting
fit_size = 12
coeff = np.polyfit(x, close, fit_size)
poly = np.poly1d(coeff)
x_poly = np.linspace(x.min(), x.max(), fit_size+1)
y_poly = poly(x_poly)
print(y_poly)

# plotting the historical closing prices
plt.plot(x, close, '.', label='Data')
plt.plot(x_poly, y_poly, '-', label='Fitting Data')
plt.xlabel('Dates from '+str(dates[0])+' to '+str(dates[len(dates)-1]))
plt.ylabel('Closing Price')
plt.title('Tesla')
plt.show()