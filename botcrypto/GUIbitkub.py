# GUIbitkub.py


import requests
from pprint import pprint
import time
from songline import Sendline
token = 'your token'
messenger = Sendline(token)

line_condition = True


API_HOST = 'https://api.bitkub.com'
mycoin = ['THB_BTC',
          'THB_ETH',
          'THB_DOGE']



condition = {'THB_BTC':{'buy':1500000,'sell':1500000},
             'THB_ETH':{'buy':100000,'sell':150000},
             'THB_DOGE':{'buy':6,'sell':8},}

#print(condition['THB_BTC'])

def CheckCondition(coin,price):
    #coin='THB_BTC', price = 1500000
    text = ''
    check_buy = condition[coin]['buy']
    if price <=check_buy:
        txt = '{} ราคาลงแล้ว เหลือ: {} รีบซื้อด่วน!\n(ราคาที่อยากได้: {})'.format(coin,price,check_buy)
        #print(txt)
        text += txt +'\n--------'
    check_sell = condition[coin]['sell']
    if price >=check_sell:
        txt = '{} ราคาขี้นแล้ว ล่าสุด: {} รีบขายด่วน!\n(ราคาที่อยากขาย: {})'.format(coin,price,check_sell)
        #print(txt)
        text += txt +'\n--------'

    return text


current_text = ''



def CheckPrice():
    global current_text
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result['THB_BTC'])

    alltext = '\n'
    text_line = ''
    

    for c in mycoin:
        #sym = 'THB_BTC'
        sym = c 
        data = result[sym]
        last = data['last']
        #print(data)
        #print(sym, last)
        pchange = data['percentChange']
        text = '{} price: {:,.3f} ({})'.format(sym,last,pchange)
        alltext += text + '\n' #alltext = alltext + text
        if line_condition == True:
            if c in condition:
                checktext = CheckCondition(c,last)
                if len(checktext) > 0:
                    text_line += checktext
                    messenger.sendtext(alltext)
                    
                    
    if line_condition == True and current_text != text_line :
        print('Condition: ',text_line)
        current_text = text_line
        #sendline
        messenger.sendtext(text_line)
            
        

    v_result.set(alltext)
    #print('-----')
    R1.after(500,CheckPrice)
    #.after คือการทำให้ R1 มีการ refresh ทุก 500 ms เรียกฟังชัน CheckPrice





######################GUI##################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x600')
GUI.title('เช็คราคาจาก Bitkub')

FONT1 = ('Angsana New',30)

L1 = ttk.Label(text='ราคา bitkub ล่าสุด',font=FONT1)
L1.pack()

#B1 = ttk.Button(GUI,text='Check',command=CheckPrice)
#B1.pack(ipadx=20 , ipady=10)


v_result = StringVar()
v_result.set ('---------result-----------')


R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()

#Run ฟังชันทุกครั้งที่เปิด
CheckPrice()
GUI.mainloop()





