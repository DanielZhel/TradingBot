import datetime
from OKEXAPI.MarketData import MarketAPI
import pandas as pd

def InstrumentData (instId, bar, limit):
    marketData = MarketAPI(flag="0", domain="https://www.okx.com", debug = True)
    cs = marketData.get_candlesticks(instId= instId,bar=bar, limit=limit)
    hist= []
    ts = []
    i= 0
    while i<limit-1:
        ts  = float(cs["data"][i][0])/1000
        time = datetime.datetime.fromtimestamp(ts)
        # ts.append(time)
        op = float((cs["data"])[i][1])
        hi = float((cs["data"])[i][2])
        lo = float((cs["data"])[i][3])
        cl = float((cs["data"])[i][4])
        a = {"time":time, "open":op, "high":hi, "low":lo,  "close":cl}
        hist.append(a) 
        
        i = i+1
    
    hist.reverse()
    instData= pd.DataFrame(hist)
    
    return instData




