
from numpy import size
import TradingBot as tb
from tkinter import *
from tkinter import ttk
import InstrumentsList as lst

instruments1 = lst.get_instruments() 
instruments=[]
choosen_insts = [] 


root = Tk()
root.title("Three Screen Strategy Test")
root.geometry("500x250") 

firstlabel = ttk.Label(text="First TimeFrame")
firstlabel.pack(anchor=E, padx=2, pady=2)
entry_firstTF = ttk.Entry()
entry_firstTF.pack(anchor=E, padx=1, pady=1)

secondlabel = ttk.Label(text="Second TimeFrame")
secondlabel.pack(anchor=E, padx=2, pady=2)
entry_secondTF = ttk.Entry()
entry_secondTF.pack(anchor=E, padx=2, pady=2)

ema_period_label = ttk.Label(text="EMA Period")
ema_period_label.pack(anchor=E, padx=2, pady=2)
entry_ema_period = ttk.Entry()
entry_ema_period.pack(anchor=E, padx=2, pady=2)

high_stoch_label = ttk.Label(text="Upper Stoch Zone")
high_stoch_label.pack(anchor=E, padx=2, pady=2)
high_stoch = ttk.Entry()
high_stoch.pack(anchor=E, padx=2, pady=2)

low_stoch_label = ttk.Label(text="Lower Stoch Zone")
low_stoch_label.pack(anchor=E, padx=2, pady=2)
low_stoch = ttk.Entry()
low_stoch.pack(anchor=E, padx=2, pady=2)

up_range_label = ttk.Label(text="EMA range for LONG(%)")
up_range_label.pack(anchor=E, padx=2, pady=2)
up_range = ttk.Entry()
up_range.pack(anchor=E, padx=2, pady=2)  

lo_range_label = ttk.Label(text="EMA range for SHORT(%)")
lo_range_label.pack(anchor=E, padx=2, pady=2)
lo_range = ttk.Entry()
lo_range.pack(anchor=E, padx=2, pady=2)  



def bot_start():
    choosen_insts.clear()
    for i in range(len(instruments)):
        if(instruments[i].get() != ""):
            choosen_insts.append(instruments[i].get()) 
    first_timeframe = entry_firstTF.get()
    second_timeframe = entry_secondTF.get() 
    high_stoch_level = float(high_stoch.get())
    low_stoch_level = float(low_stoch.get())
    ema_period = int(entry_ema_period.get())
    up_range_ema = float(up_range.get())
    lo_range_ema = float(lo_range.get())
    
    tb.bot_start(choosen_insts,
                 first_timeframe, 
                 second_timeframe, 
                 ema_period,
                 high_stoch_level,
                 low_stoch_level,
                 up_range_ema,
                 lo_range_ema)
    
for i in range(len(instruments1)):
    inst = StringVar()
    check_box = ttk.Checkbutton(text=instruments1[i], variable=inst,onvalue=instruments1[i], offvalue="")
    check_box.pack(padx=6, pady=6, anchor=NW)
    instruments.append(inst)
    
button = ttk.Button(text="Start", command=bot_start)
button.pack(side=BOTTOM)

root.mainloop()





