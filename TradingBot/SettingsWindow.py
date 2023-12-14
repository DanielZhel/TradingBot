import InstrumentsList as lst
from tkinter import *
from tkinter import font
import TradingBot as tb
from PIL import Image, ImageTk

instruments1 = lst.get_instruments() 
instruments=[]
choosen_insts = [] 




window = Tk()
window.title("Three Screen Strategy Test")
window.geometry("750x400")
window.resizable(width=FALSE, height=FALSE)
window["bg"]="linen"

image = Image.open("Image\help.jpg")
size=(350,270)
image.thumbnail(size)
photo = ImageTk.PhotoImage(image)
label = Label(window, image=photo)
label.place(x=360, y=100)


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

firstlabel = Label(text="1.First TimeFrame(2H)", font=font1)
firstlabel['bg']="linen"
firstlabel.place(x=180, y =0)
entry_firstTF = Entry()
entry_firstTF.place(x=180, y= 20)

secondlabel = Label(text="2.Second TimeFrame(30m)", font=font1)
secondlabel.place( x=180, y =50)
secondlabel['bg']="linen"
entry_secondTF = Entry()
entry_secondTF.place(x=180, y =70)

ema_period_label = Label(text="3.EMA Period(26)", font=font1)
ema_period_label.place( x=180, y =100)
ema_period_label['bg']="linen"
entry_ema_period = Entry()
entry_ema_period.place( x=180, y =120)

high_stoch_label = Label(text="4.Upper Stoch Level(80)", font=font1)
high_stoch_label.place(x=180, y =150)
high_stoch_label['bg']="linen"
high_stoch = Entry()
high_stoch.place(x=180, y =170)

low_stoch_label = Label(text="5.Lower Stoch Level(20)", font=font1)
low_stoch_label.place(x=180, y=200)
low_stoch_label['bg']="linen"
low_stoch = Entry()
low_stoch.place(x=180, y=220)

up_range_label = Label(text="6.EMA range for LONG(%)(3)", font=font1)
up_range_label.place( x=180, y=250)
up_range_label['bg']="linen"
up_range = Entry()
up_range.place(x=180, y=270)  

lo_range_label = Label(text="7.EMA range for SHORT(%)(3)", font=font1)
lo_range_label.place(x=180, y=300)
lo_range_label['bg']="linen"
lo_range = Entry()
lo_range.place(x=180, y=320)  

rm_label = Label(text="8.R\M(3)", font=font1)
rm_label.place(x=180, y=350)
rm_label['bg']="linen"
rm = Entry()
rm.place(x=180, y=370) 

high_stop_label = Label(text="9.From high to stop(%)(0.03)", font=font1)
high_stop_label.place(x=360, y=0)
high_stop_label['bg']="linen"
high_stop = Entry()
high_stop.place(x=360, y=20) 

low_stop_label = Label(text="10.From low to stop(%)(0.03)", font=font1)
low_stop_label.place(x=360, y=50)
low_stop_label['bg']="linen"
low_stop = Entry()
low_stop.place(x=360, y=70) 

min_stop_label = Label(text="11.Minimum stop percent(%)(0.3)", font=font1)
min_stop_label.place(x=540, y=0)
min_stop_label['bg']="linen"
min_stop = Entry()
min_stop.place(x=540, y=20) 


def bot_start():
    choosen_insts.clear()
    for i in range(len(instruments)):
        if(instruments[i].get() != ""):
            choosen_insts.append(instruments[i].get()) 
     
    if(entry_firstTF.get() == ""):
        first_timeframe = "2H"
    else:
        first_timeframe = entry_firstTF.get()
        
    if(entry_secondTF.get() == ""):
        second_timeframe = "30m"
    else:
        second_timeframe = entry_secondTF.get()
        
    if(high_stoch.get()== ""):
        high_stoch_level = 80
    else:
        high_stoch_level = float(high_stoch.get())
        
    if(low_stoch.get()== ""):
        low_stoch_level = 20
    else:
        low_stoch_level = float(low_stoch.get())
    
    if(entry_ema_period.get()== ""):
        ema_period = 26
    else:
        ema_period = int(entry_ema_period.get())

    if(up_range.get()== ""):
        up_range_ema = 3
    else:
        up_range_ema = float(up_range.get())
        
    if(lo_range.get()== ""):
        lo_range_ema = 3
    else:
        lo_range_ema = float(lo_range.get())
     
    if(rm.get()== ""):
        risk = 3
    else:
        risk=float(rm.get())
        
    if(high_stop.get()== ""):
        high_stop_percent = 0.03
    else:
        high_stop_percent=float(high_stop.get())
        
    if(low_stop.get()== ""):
        low_stop_percent=0.03
    else:
        low_stop_percent = float(low_stop.get())
        
    if(min_stop.get()== ""):
        min_stop_percent=0.3
    else:
        min_stop_percent = float(min_stop.get())
        
    tb.bot_start(choosen_insts,
                 first_timeframe, 
                 second_timeframe, 
                 ema_period,
                 high_stoch_level,
                 low_stoch_level,
                 up_range_ema,
                 lo_range_ema,
                 risk,
                 high_stop_percent,
                 low_stop_percent,
                 min_stop_percent)
    
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
    check_box.configure(state="normal")


    
button = Button(text="Start", command=bot_start)
button.place(x=50,y=360)

scrollbar.config(command=inst_text.yview)
window.mainloop()


    



