import pandas as pd
import glob, re, csv, datetime
import matplotlib.pyplot as plt

class Transform():
    def append_data(df_list):
        patterns= ["EUR.*","AUD.*", "BRL.*","ETH.*", "RUB.*","CNY.*", "CLP.*","BTC.*"]
        dfs = []
        big_frame=[]
        for pattern in patterns:
            exchange = [string for string in df_list if re.match(pattern, string)]
            for filename in exchange:
                dfs.append(pd.read_csv(filename))
                big_frame = pd.concat(dfs, ignore_index=True)
        print(big_frame)
        big_frame['Datetime'] = pd.to_datetime(big_frame['Datetime'],format='ISO8601')
        #big_frame.sort_values(by='Datetime',ascending=True, inplace=True)       
        #big_frame.drop_duplicates(subset='Datetime', inplace=True, keep='first', ignore_index=True)
        #big_frame.to_csv("data/Consolidado_euro.csv")
        #big_frame.set_index(pd.DatetimeIndex(big_frame['Datetime']))
        #plt.plot(big_frame.index, big_frame['Close'])
        #plt.xlabel("Date")
        #plt.ylabel("Closing Price")
        #plt.title("Euro")
        #plt.show()