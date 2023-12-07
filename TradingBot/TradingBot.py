import ChartsInit as init
import Data as data
import Indicators as ind

# instruments1= ["XRP-USDT",
#                "SOL-USDT",
#                "ADA-USDT", 
#                "CRO-USDT", 
#                "MATIC-USDT", 
#                "LOOKS-USDT",
#                "ETH-USDT", 
#                "FIL-USDT", 
#                "LTC-USDT", 
#                "DOT-USDT"]
# instruments1= ["XRP-USDT"]
instruments1= ["LOOKS-USDT",
               "ETH-USDT", 
               "FIL-USDT", 
               "LTC-USDT", 
               "DOT-USDT"]
# Временной интервал
firstTF = "1H"
secondTF = "15m"
emaPeriod = 26

for i in range(len(instruments1)):
    instData1 = data.InstrumentData(instruments1[i], firstTF, 100)
    instData2 = data.InstrumentData(instruments1[i], secondTF, 300)
    emaValues = ind.GetEMAValues(instData1, 26)
    macdValues  = ind.GetMACDValues(instData1)
    stochValues = ind.GetStochValues(instData2)
    init.ChartsInit(instData1, instData2, macdValues, emaValues, stochValues, i, instruments1, firstTF, secondTF)
