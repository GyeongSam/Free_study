def fee(min,km):
    fee_1=(min//10 +(1 if min%10!=0 else 0))*1200
    fee_2=(min//30 +(1 if min%30!=0 else 0))*525
    fee_3=km*170 if km<=100 else (km-100)*85+100*170
    return fee_1+fee_2+fee_3

print(fee(600,50))