import yfinance as yf
import pandas as pd
from datetime import datetime
from transform import Transform
import glob



t = datetime.now().strftime('%Y%m%d')
tickers = ["EUR=X","BRL=X","AUD=X","CLP=X","CNY=X","RUB=X","BTC-USD","ETH-USD"]
#executando todo o dia no mesmo horario eu posso simplesmente fazer o appen dos dados diarios
for ticker in tickers:
    forex =yf.Ticker(ticker)
    df_forex = forex.history(period="7d", interval="1m")
    df_forex.to_csv(f'{ticker}-{t}.csv')
all_files = glob.glob("*.csv")
Transform.append_data(all_files)
    
    #print(df_forex.equals(df))
    #print(df_forex.reset_index(drop=True).compare((df.reset_index(drop=True))))
    #print(f'{ticker}:{df.shape}')
    #print(f'{ticker}-{t}:{df_forex.shape}')