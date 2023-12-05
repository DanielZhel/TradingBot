import ChartsInit as init
import Data as data
import Indicators as ind




inst= ["XRP-USDT","SOL-USDT","ADA-USDT", "CRO-USDT", "MATIC-USDT"]

# Временной интервал
firstTF = "2H"
secondTF = "30m"
emaPeriod = 26

for i in range(len(inst)):
    instData1 = data.InstrumentData(inst[i], firstTF, 100)
    instData2 = data.InstrumentData(inst[i], secondTF, 300)
    emaValues = ind.GetEMAValues(instData1, 26)
    macdValues  = ind.GetMACDValues(instData1)
    stochValues = ind.GetStochValues(instData2)
    init.ChartsInit(instData1, instData2, macdValues, emaValues, stochValues)
