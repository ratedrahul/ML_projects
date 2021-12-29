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



stock_name = 'SBIN'
days = 20
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

# print(len(close))
total_days = [[x] for x in range(1,len(close)+1)]

lin_svr = SVR(kernel = 'linear',C = 1000.0)
lin_svr.fit(total_days,close)


poly_svr = SVR(kernel = 'poly',C = 1000.0,degree= 2)
poly_svr.fit(total_days,close)


rbf_svr = SVR(kernel = 'rbf',C = 1000.0, gamma = 0.85)
rbf_svr.fit(total_days,close)


plt.figure(figsize=(16,8))
plt.scatter(total_days, close,color = 'black',label = 'Data')
plt.plot(total_days, rbf_svr.predict(total_days), color = 'green', label = 'RBF Model')
plt.plot(total_days, poly_svr.predict(total_days), color = 'red', label = 'Poly Model')
plt.plot(total_days, lin_svr.predict(total_days), color = 'orange', label = 'Linear Model')

plt.xlabel('Days')
plt.ylabel('Close')
plt.legend()
plt.show()


	# exec(f'stock_values.append(df.loc["{i}"])')
	# p
	# print(stock_values)
	# print(x)

# 	for i in t_days:
	# exec(f'df = pd.read_csv(i)')
	# df
# print(t_days)


# Extract_Data()

# exec(f"df = pd.read_csv('{files[0]}', names = ['symbol','date','open','high','low','close','volume'],index_col=0)")
