while(True):
    Money = input("请依次输入币值与符号(￥/$)或输入exit退出：")
    MoneyType = Money[-1]
    #print(MoneyType)
    
    if(MoneyType == '￥'):
        number = float(Money[0:-1])
        Umoney0 =  0.1452 * number
        Umoney = str("%.3f"%Umoney0)
        print("可兑换的美元为:"+ Umoney +'$')
    
    elif(MoneyType == '$'):
        number = float(Money[0:-1])
        Cmoney0 = 6.8833 * number
        Cmoney = str("%.3f"%Cmoney0)
        print("可兑换的人民币为:"+Cmoney+'￥')
        
    elif(Money == 'exit'):
        break
    
    elif MoneyType != '￥' or '$' :
        print("输入有误")
