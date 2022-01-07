from binance import Client
from songline import Sendline
import time

token = 'Your_Token'
messenger = Sendline(token)

api_key = 'Your_api_key'
api_secret = 'Your_api_secret'
client = Client(api_key, api_secret)

# get all symbol prices
def CheckPrice():
     prices = client.get_all_tickers()

     mycoin1 = ['BTCUSDT']
     namecoin1 = ['BTC']
     mycoin2 = ['BNBUSDT']
     namecoin2 = ['BNB']
     mycoin3 = ['ETHUSDT']
     namecoin3 = ['ETH']

     alltext = ''

     for p in prices:
          for c in mycoin1:
             sym = c
             if p['symbol'] == sym:
                 pc = float(p['price'])
                 rate = 33.20
                 cal = pc*rate
                 for N in namecoin1:
                     print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N,cal))
                     text = 'เหรียญ {} ราคา {:,.2f} บาท'.format(N,cal)
                     alltext += text + '\n\n'
                     
          for c in mycoin2:
             sym = c
             if p['symbol'] == sym:
                 pc = float(p['price'])
                 rate = 33.20
                 cal = pc*rate
                 for N in namecoin2:
                     print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N,cal))
                     text = 'เหรียญ {} ราคา {:,.2f} บาท'.format(N,cal)
                     alltext += text + '\n\n'
                     
          for c in mycoin3:
               sym = c
               if p['symbol'] == sym:
                 pc = float(p['price'])
                 rate = 33.20
                 cal = pc*rate
                 for N in namecoin3:
                      print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N,cal))
                      text = 'เหรียญ {} ราคา {:,.2f} บาท'.format(N,cal)
                      alltext += text + '\n\n'
               
     v_result.set(alltext)
     print('----')
     R1.after(500,CheckPrice)
     
#หาเหรียญ
def FindCoin():

     coin = TI1.get()
     COIN = coin.upper()
     COINUSDT = COIN + 'USDT'
     Tcoin = [COINUSDT]

     prices = client.get_all_tickers()

     for p in prices:
          for c in Tcoin:
             sym = c
             if p['symbol'] == sym:
                 pc = float(p['price'])
                 rate = 33.20
                 cal = pc*rate
                 N = COIN
                 print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N,cal))
                 text2 = 'เหรียญ {}  ราคา {:,.2f} บาท\n\n'.format(N,cal)
     v2_result.set(text2)
     R2.after(500,FindCoin)
     
#SendLine
def SendLine():
    coin = TI1.get()
    COIN = coin.upper()
    COINUSDT = COIN + 'USDT'
    Tcoin = [COINUSDT]

    prices = client.get_all_tickers()

    for p in prices:
        for c in Tcoin:
            sym = c
            if p['symbol'] == sym:
                pc = float(p['price'])
                rate = 33.20
                cal = pc * rate
                N = COIN
                print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N, cal))
                text2 = 'เหรียญ {}  ราคา {:,.2f} บาท\n\n'.format(N, cal)
                text3 = '\nเหรียญ {} \nราคา {:,.2f} บาท'.format(N, cal)
                    
    v2_result.set(text2)
    messenger.sendtext(text3)

#GUI#

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x580')
GUI.title('COIN PRICE FROM BINANCE')

FONT1 = ('Tahoma' ,20,'bold')
FONT2 = ('Tahoma' ,15)
FONT3 = ('' ,15)
FONT4 = ('' ,5)

L = ttk.Label(GUI,text ='',font = FONT4)
L.pack()
L1 = ttk.Label(GUI,text ='ราคาเหรียญ',font = FONT1)
L1.pack()

L2 = ttk.Label(GUI,text ='',font = FONT1)
L2.pack()

v_result = StringVar()
v_result.set('เหรียญ BTC ราคา - - - บาท\n\nเหรียญ ETH ราคา - - - บาท\n\nเหรียญ BNB ราคา - - - บาท\n\n')
R1 = ttk.Label(textvariable = v_result,font = FONT3)
R1.pack()

CheckPrice()

#หาเหรียญ
L3 = ttk.Label(GUI,text ='ค้นหาเหรียญที่ต้องการ\n',font = FONT1)
L3.pack()

v2_result = StringVar()
v2_result.set('กรุณาใส่ชื่อเหรียญที่ต้องการ\n\n')
R2 = ttk.Label(textvariable = v2_result,font = FONT3)
R2.pack()

TI1 = ttk.Entry(GUI)
TI1.pack(ipadx=60,ipady=6)
L4 = ttk.Label(GUI,text ='',font = FONT3)
L4.pack()

B2 = ttk.Button(GUI,text='Check!',command= FindCoin)
B2.pack(ipadx=100,ipady=5)
L5 = ttk.Label(GUI,text ='',font = FONT4)
L5.pack()

B3 = ttk.Button(GUI,text='SendLine',command= SendLine)
B3.pack(ipadx=100,ipady=5)


GUI.mainloop()
