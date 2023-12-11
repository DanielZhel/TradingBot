import InstrumentsList as lst
from tkinter import *
from tkinter import font
import TradingBot as tb

instruments1 = lst.get_instruments() 
instruments=[]
choosen_insts = [] 


window = Tk()
window.title("Three Screen Strategy Test")
window.geometry("420x400")
window.resizable(width=FALSE, height=FALSE)

font1 = font.Font(family= "Arial", size=9, weight="bold", slant="roman")

frame = Frame(window)
frame.place(x=10,y=10, width=150, height=300)

scrollbar=Scrollbar(frame, orient="vertical")
scrollbar.pack(fill=BOTH, side=RIGHT)

inst_text =Text(frame, yscrollcommand=scrollbar.set, background="lightblue")
inst_text.pack(anchor=NW)
inst_text.configure(state=DISABLED, cursor='')
inst_text.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=inst_text.yview)

firstlabel = Label(text="First TimeFrame(2H)", font=font1)
firstlabel.place(x=250, y =0)
entry_firstTF = Entry()
entry_firstTF.place(x=250, y= 20)

secondlabel = Label(text="Second TimeFrame(30m)", font=font1)
secondlabel.place( x=250, y =50)
entry_secondTF = Entry()
entry_secondTF.place(x=250, y =70)

ema_period_label = Label(text="EMA Period(26)", font=font1)
ema_period_label.place( x=250, y =100)
entry_ema_period = Entry()
entry_ema_period.place( x=250, y =120)

high_stoch_label = Label(text="Upper Stoch Level(80)", font=font1)
high_stoch_label.place(x=250, y =150)
high_stoch = Entry()
high_stoch.place(x=250, y =170)

low_stoch_label = Label(text="Lower Stoch Level(20)", font=font1)
low_stoch_label.place(x=250, y=200)
low_stoch = Entry()
low_stoch.place(x=250, y=220)

up_range_label = Label(text="EMA range for LONG(%)(3)", font=font1)
up_range_label.place( x=250, y=250)
up_range = Entry()
up_range.place(x=250, y=270)  

lo_range_label = Label(text="EMA range for SHORT(%)(3)", font=font1)
lo_range_label.place(x=250, y=300)
lo_range = Entry()
lo_range.place(x=250, y=320)  

rm_label = Label(text="R\M(3)", font=font1)
rm_label.place(x=250, y=350)
rm = Entry()
rm.place(x=250, y=370) 


def bot_start():
    choosen_insts.clear()
    for i in range(len(instruments)):
        if(instruments[i].get() != ""):
            choosen_insts.append(instruments[i].get()) 
     
    if(entry_firstTF.get() == ""):
        first_timeframe = "2H"
        second_timeframe = "30m"
        high_stoch_level = 80
        low_stoch_level = 20
        ema_period = 26
        up_range_ema = 3
        lo_range_ema = 3
        risk = 3
    else:
        first_timeframe = entry_firstTF.get()
        second_timeframe = entry_secondTF.get()
        high_stoch_level = float(high_stoch.get())
        low_stoch_level = float(low_stoch.get())
        ema_period = int(entry_ema_period.get())
        up_range_ema = float(up_range.get())
        lo_range_ema = float(lo_range.get())
        risk=float(rm.get())
    tb.bot_start(choosen_insts,
                 first_timeframe, 
                 second_timeframe, 
                 ema_period,
                 high_stoch_level,
                 low_stoch_level,
                 up_range_ema,
                 lo_range_ema,
                 risk)
  
for i in range(len(instruments1)):
    
    inst = StringVar()
    check_box = Checkbutton(
                                text=instruments1[i], 
                                variable=inst,
                                onvalue=instruments1[i], 
                                offvalue="",background="lightblue")
    inst_text.window_create(END, window=check_box)
    inst_text.insert(END, '\n')
    instruments.append(inst)
    
    
button = Button(text="Start", command=bot_start)
button.place(x=160,y=360)

scrollbar.config(command=inst_text.yview)
window.mainloop()





