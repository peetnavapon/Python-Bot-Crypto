#algocheck.py

condition = {'THB_BTC':{'buy':1400000,'sell':1700000},
             'THB_ETH':{'buy':120000,'sell':150000},
             'THB_DOGE':{'buy':5,'sell':8},}

#print(condition['THB_BTC'])

def CheckCondition(coin,price):
    #coin='THB_BTC', price = 1500000
    text = ''
    check_buy = condition[coin]['buy']
    if price <=check_buy:
        txt = '{} ราคาลงแล้ว เหลือ: {} รีบซื้อด่วน!\n(ราคาที่อยากได้: {})'.format(coin,price,check_buy)
        print(txt)
        text += txt +'\n--------'
    check_sell = condition[coin]['sell']
    if price >=check_sell:
        txt = '{} ราคาขี้นแล้ว ล่าสุด: {} รีบขายด่วน!\n(ราคาที่อยากขาย: {})'.format(coin,price,check_sell)
        print(txt)
        text += txt +'\n--------'

    return text

CheckCondition('THB_ETH',1510)
