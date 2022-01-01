import pandas as pd   
import numpy as np   
import os
from sklearn.svm import SVR
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


os.chdir(r'F:\new_share_data')
files = os.listdir()
files.sort(reverse= True)


# df = pd.read_csv(files[0], names = ['symbol','date','open','high','low','close','volume'],index_col=0)

    # exec((f'df{count}=pd.read_csv({i})'))
    # exec((f"df{count}.columns = ['Symbol','Date','Open','High','Low','Close','Volume']"))
    # exec(f'df{count}=df{count}.set_index(df{count}["Symbol"])')
# print(files)
# def Extract_Data(stock_name = 'SBIN',days = 30):



stock_name = 'ASIANPAINT'
days = 30
t_days = files[:days]
# global stock_values
stock_values = []
# exec(f"df_{stock_name}")
# global df
# exec(f'stock_{stock_name}')dsfak
for i in t_days:
	# exec(f"df = pd.read_csv('{i}')")
	exec(f"df = pd.read_csv('{i}', names = ['symbol','date','open','high','low','close','volume'],index_col=0)")
	# exec(f'stock_values.append(df.loc["{stock_name}"])')
	# exec(f'stock_values.append(df.loc["{stock_name}"][-2])')
	exec(f'stock_values.append([str(df.loc["{stock_name}"][0]),df.loc["{stock_name}"][-2]])')
	# stock_values.append()
	# exec(f'')
	# exec('This printu')

total_days = []
close = []
# total_days = [[xk]]
for x,y in stock_values[::-1]:
	# print(x,y)
	# total_days.append([x])
	# total_days.append([float(x)])
	# print(x)
	close.append(float(y))


# plt.figure(figsize = (16,8))
# plt.title('Close Price')
# plt.plot(close)
# plt.xlabel('date')
# plt.ylabel('Close')
# plt.show()

print(df.columns)
def SMA(data,period = 30, column = 'close'):
	# return data[column].rolling(window = period).mean()
	return df[column].rolling(window = period).mean()
	# return data[column].rolling(window = period).mean()
	# print(data[column])
	# return da
	# pass

print(type(close))

close_d = pd.DataFrame(close)
df['SMA30'] = SMA(close_d)
print(df.columns)


def strategy(df):
	buy = []
	sell = []
	flag = 0 
	buy_price = 0   
	for i in range(0,len(df)):
		if df['SMA30'][i] > df['close'][i] and flag == 0:
			buy.append(df['close'][i])
			sell.append(np.nan)
			buy_price = df['close'][i]
			flag = 1 
		elif df['SMA30'][i] > df['close'][i] and flag == 1 and buy_price < df['close'][i]:
			sell.append(df['close'][i]) 
			buy.append(np.nan)
			buy_price = 0 
			flag = 0 
		else:
			sell.append(np.nan)
			buy.append(np.nan)

	return (buy,sell)

strat = strategy(df)
df['Buy'] = strat[0]
df['[Sell'] = strat[1]



